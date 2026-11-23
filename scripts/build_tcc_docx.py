#!/usr/bin/env python3
"""
Monta o .docx final do TCC a partir dos fontes Markdown em docs/tcc/.

Pipeline:
  1. Gera/ajusta um reference-doc ABNT (estilos, margens) para o pandoc.
  2. Assembla um master.md (ordem ABNT; Mermaid -> imagem; remove o Sumário manual).
  3. pandoc master.md -> build/corpo.docx (usa o reference-doc).
  4. python-docx: prepende capa + folha de rosto + folha de aprovação,
     insere o Sumário (campo TOC do Word), aplica numeração de página a partir
     da Introdução, e salva docs/tcc/TCC_Gabriel_Aragao_2026.docx.

Uso: ./venv/bin/python scripts/build_tcc_docx.py   (com pandoc no PATH)
"""
from __future__ import annotations
import subprocess, sys, re, copy
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION_START
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph as _Par

ROOT = Path(__file__).resolve().parents[1]
TCC = ROOT / "docs" / "tcc"
BUILD = TCC / "build"
ASSETS = TCC / "assets"
OUT = TCC / "TCC_Gabriel_Aragao_2026.docx"

ANO = "2026"
AUTOR = "GABRIEL ARAGÃO CORREIA DE ARAÚJO"
TITULO = ("IMPLEMENTAÇÃO E AVALIAÇÃO DE AUTENTICAÇÃO PÓS-QUÂNTICA EM APLICAÇÕES "
          "WEB: COMPARAÇÃO DE DESEMPENHO ENTRE ALGORITMOS NIST PQC")
NATUREZA = ("Trabalho de Conclusão de Curso apresentado ao Curso de Graduação em "
            "Sistemas de Informação da Universidade Federal de Pernambuco, como "
            "requisito parcial para obtenção do título de bacharel em Sistemas de "
            "Informação.")
ORIENTADOR = "Prof. Vinícius Cardoso Garcia"
INSTITUICAO = "Universidade Federal de Pernambuco"

ORDER = [
    "00-resumo-abstract.md",
    "00-sumario-listas.md",
    "01-introducao.md",
    "02-trabalhos-relacionados.md",
    "03-referencial-teorico.md",
    "04-metodologia.md",
    "05-resultados.md",
    "06-conclusao.md",
    "referencias.md",
    "apendice-A-protocolo-revisao.md",
]
MERMAID_IMG = {
    "04-metodologia.md": ASSETS / "figura-4-1.png",
    "05-resultados.md": ASSETS / "figura-5-1.png",
}
PRETEXTUAL_TITLES = {"RESUMO", "ABSTRACT", "LISTA DE FIGURAS",
                     "LISTA DE TABELAS", "LISTA DE QUADROS"}
MERMAID_RE = re.compile(r"```mermaid.*?```", re.DOTALL)


# --- 1. reference-doc ABNT ---------------------------------------------------- #
def build_reference_doc(path: Path) -> None:
    raw = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                         capture_output=True, check=True).stdout
    path.write_bytes(raw)
    doc = Document(str(path))
    for sec in doc.sections:
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.top_margin, sec.bottom_margin = Cm(3), Cm(2)
        sec.left_margin, sec.right_margin = Cm(3), Cm(2)
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    rpr = normal.element.get_or_add_rPr().get_or_add_rFonts()
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rpr.set(qn(attr), "Times New Roman")
    pf = normal.paragraph_format
    pf.line_spacing = 1.5
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.first_line_indent = Cm(1.25)
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        st = doc.styles[name]
        st.font.name = "Times New Roman"
        st.font.size = Pt(12)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        hpf = st.paragraph_format
        hpf.first_line_indent = Cm(0)
        hpf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        hpf.space_before = Pt(12)
        hpf.space_after = Pt(6)
        hpf.keep_with_next = True
    doc.save(str(path))


# --- 2. master.md ------------------------------------------------------------- #
def assemble_master(master_path: Path) -> None:
    chunks = []
    for fname in ORDER:
        text = (TCC / fname).read_text(encoding="utf-8")
        if fname == "00-sumario-listas.md":
            idx = text.find("# SUMÁRIO")
            if idx != -1:
                text = text[:idx].rstrip() + "\n"
        if fname in MERMAID_IMG:
            img = MERMAID_IMG[fname]
            text = MERMAID_RE.sub(f"![]({img.as_posix()})", text, count=1)
        chunks.append(text.strip())
    master_path.write_text("\n\n".join(chunks) + "\n", encoding="utf-8")


# --- 3. pandoc ---------------------------------------------------------------- #
def run_pandoc(master: Path, ref: Path, out: Path) -> None:
    subprocess.run([
        "pandoc", str(master), "-o", str(out),
        "--reference-doc", str(ref),
        "--resource-path", str(TCC),
        "-f", "markdown+tex_math_dollars+pipe_tables",
    ], check=True)


# --- 4. front matter + TOC + numeração ---------------------------------------- #
def _set_font(run, size=12, bold=False):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.font.bold = bold
    rpr = run._element.get_or_add_rPr().get_or_add_rFonts()
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rpr.set(qn(a), "Times New Roman")


def _mk(parent, text="", align=WD_ALIGN_PARAGRAPH.CENTER, bold=False, size=12,
        before=0, after=0, indent_left=None):
    par = _Par(OxmlElement("w:p"), parent)
    par.alignment = align
    pf = par.paragraph_format
    pf.first_line_indent = Cm(0)
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.5
    if indent_left is not None:
        pf.left_indent = Cm(indent_left)
    if text:
        _set_font(par.add_run(text), size=size, bold=bold)
    return par


def _page_break(parent):
    par = _mk(parent)
    par.add_run().add_break(WD_BREAK.PAGE)
    return par


def build_front_matter(anchor, parent):
    els = []
    for ln in ("UNIVERSIDADE FEDERAL DE PERNAMBUCO", "CENTRO DE INFORMÁTICA",
               "GRADUAÇÃO EM SISTEMAS DE INFORMAÇÃO"):
        els.append(_mk(parent, ln, bold=True))
    els += [_mk(parent) for _ in range(6)]
    els.append(_mk(parent, AUTOR, bold=True))
    els += [_mk(parent) for _ in range(6)]
    els.append(_mk(parent, TITULO, bold=True))
    els += [_mk(parent) for _ in range(10)]
    els.append(_mk(parent, "Recife"))
    els.append(_mk(parent, ANO))
    els.append(_page_break(parent))

    els.append(_mk(parent, AUTOR, bold=True))
    els += [_mk(parent) for _ in range(6)]
    els.append(_mk(parent, TITULO, bold=True))
    els += [_mk(parent) for _ in range(3)]
    els.append(_mk(parent, NATUREZA, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent_left=8))
    els += [_mk(parent) for _ in range(2)]
    els.append(_mk(parent, f"Orientador: {ORIENTADOR}",
                   align=WD_ALIGN_PARAGRAPH.LEFT, indent_left=8))
    els += [_mk(parent) for _ in range(8)]
    els.append(_mk(parent, "Recife"))
    els.append(_mk(parent, ANO))
    els.append(_page_break(parent))

    els.append(_mk(parent, AUTOR, bold=True))
    els += [_mk(parent) for _ in range(4)]
    els.append(_mk(parent, TITULO, bold=True))
    els += [_mk(parent) for _ in range(3)]
    els.append(_mk(parent, NATUREZA, align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent_left=8))
    els += [_mk(parent) for _ in range(2)]
    els.append(_mk(parent, "Aprovado em: ______ / ______ / __________",
                   align=WD_ALIGN_PARAGRAPH.LEFT))
    els += [_mk(parent) for _ in range(2)]
    els.append(_mk(parent, "BANCA EXAMINADORA", bold=True))
    els += [_mk(parent) for _ in range(3)]
    membros = [
        (f"{ORIENTADOR} (Orientador)", INSTITUICAO),
        ("Prof. __________________________ (Examinador)", INSTITUICAO),
        ("Prof. __________________________ (Examinador)", INSTITUICAO),
    ]
    for nome, inst in membros:
        els.append(_mk(parent, "____________________________________________"))
        els.append(_mk(parent, nome))
        els.append(_mk(parent, inst))
        els += [_mk(parent) for _ in range(2)]
    els.append(_page_break(parent))

    for par in els:
        anchor.addprevious(par._element)


def make_toc_field(parent):
    par = _mk(parent, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = par.add_run()
    r = run._element
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = 'TOC \\o "1-3" \\h \\z \\u'
    sep = OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"), "separate")
    r.append(b); r.append(instr); r.append(sep)
    ph_r = OxmlElement("w:r"); ph_t = OxmlElement("w:t")
    ph_t.text = "Atualize o sumário no Word: clique com o botão direito > Atualizar campo."
    ph_r.append(ph_t); par._element.append(ph_r)
    end_r = OxmlElement("w:r"); end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end"); end_r.append(end); par._element.append(end_r)
    return par


def add_page_number_header(section):
    header = section.header
    header.is_linked_to_previous = False
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = "PAGE"
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    run._element.append(b); run._element.append(i); run._element.append(e)
    _set_font(run, size=10)


def finalize(corpo: Path, out: Path) -> None:
    doc = Document(str(corpo))
    body = doc.element.body
    parent = doc.paragraphs[0]._parent

    intro = None
    for p in doc.paragraphs:
        if p.style and p.style.name == "Heading 1" and re.match(r"^1[.\s]", p.text.strip()):
            intro = p
            break
    if intro is None:
        raise RuntimeError("Não encontrei o título '1. Introdução' no corpo.")

    for p in doc.paragraphs:
        if p.style and p.style.name == "Heading 1" and p.text.strip().upper() in PRETEXTUAL_TITLES:
            p.style = doc.styles["Normal"]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                _set_font(r, size=12, bold=True)

    intro._p.addprevious(_mk(parent, "SUMÁRIO", bold=True)._element)
    intro._p.addprevious(make_toc_field(parent)._element)

    final_sectPr = body.find(qn("w:sectPr"))
    sect_p = OxmlElement("w:p")
    pPr = OxmlElement("w:pPr")
    pPr.append(copy.deepcopy(final_sectPr) if final_sectPr is not None else OxmlElement("w:sectPr"))
    sect_p.append(pPr)
    intro._p.addprevious(sect_p)

    build_front_matter(body[0], parent)

    secs = doc.sections
    secs[-1].start_type = WD_SECTION_START.NEW_PAGE
    add_page_number_header(secs[-1])
    doc.save(str(out))


def main():
    BUILD.mkdir(exist_ok=True)
    for f in (MERMAID_IMG["04-metodologia.md"], MERMAID_IMG["05-resultados.md"]):
        if not f.exists():
            print(f"AVISO: figura ausente: {f}", file=sys.stderr)
    ref = BUILD / "ref-abnt.docx"
    master = BUILD / "master.md"
    corpo = BUILD / "corpo.docx"
    print("1/4 reference-doc ABNT…"); build_reference_doc(ref)
    print("2/4 master.md…"); assemble_master(master)
    print("3/4 pandoc -> corpo.docx…"); run_pandoc(master, ref, corpo)
    print("4/4 front matter + TOC + numeração…"); finalize(corpo, OUT)
    print(f"OK -> {OUT}")


if __name__ == "__main__":
    main()
