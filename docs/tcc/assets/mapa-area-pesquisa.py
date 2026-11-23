# Gera o diagrama "Mapa da Área de Pesquisa" para o slide 05 do TCC.
# Tamanho físico = área da imagem no slide (18,2 × 6,8 cm) → fontes em pt reais.
# Cada texto é medido no renderer e encolhido até caber no card (sem overflow).
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

RED = "#DB1E2F"       # cor do deck
INK = "#3A3A3A"       # títulos dos cards
BODY = "#595959"      # texto do deck
MUTED = "#8A8A8A"
CARD_BG = "#F7F7F7"
CARD_EDGE = "#DCDCDC"

CM = 1 / 2.54
W_CM, H_CM = 18.2, 6.8
fig = plt.figure(figsize=(W_CM * CM, H_CM * CM), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W_CM)
ax.set_ylim(0, H_CM)
ax.axis("off")
fig.patch.set_facecolor("white")
renderer = fig.canvas.get_renderer()


def text_fit(x, y, s, max_w, size, ha="left", **kw):
    """Desenha texto encolhendo a fonte até caber em max_w cm (mín. 7.4pt)."""
    t = ax.text(x, y, s, fontsize=size, ha=ha, va="center", **kw)
    while size > 7.4:
        bb = t.get_window_extent(renderer=renderer)
        inv = ax.transData.inverted()
        w = inv.transform((bb.x1, bb.y1))[0] - inv.transform((bb.x0, bb.y0))[0]
        if w <= max_w:
            break
        size -= 0.25
        t.set_fontsize(size)
    return t


MARGIN, GAP = 0.06, 1.27
CARD_W = (W_CM - 2 * MARGIN - 2 * GAP) / 3          # ≈ 5.16
X0 = [MARGIN + i * (CARD_W + GAP) for i in range(3)]
CARD_Y0, CARD_Y1 = 0.72, 6.70
PAD = 0.34
LINE = 0.54

cards = [
    {
        "kicker": "ANEL 1",
        "title": "Criação das primitivas",
        "body": [
            ("CRYSTALS", "bold", BODY),
            ("Kyber → ML-KEM (FIPS 203)", "normal", BODY),
            ("Dilithium → ML-DSA (FIPS 204)", "normal", BODY),
            ("Schwabe · Lyubashevsky · Ducas", "normal", BODY),
            ("NIST — padronização", "normal", BODY),
            ("Europa · EUA", "italic", MUTED),
        ],
        "note": "quem desenha os algoritmos",
        "hl": False,
    },
    {
        "kicker": "ANEL 2",
        "title": "Transporte (TLS)",
        "body": [
            ("Open Quantum Safe (liboqs)", "bold", BODY),
            ("Stebila & Mosca — Waterloo", "normal", BODY),
            ("Kampanakis (AWS) · Sikeridis", "normal", BODY),
            ("liboqs → usada neste trabalho", "italic", RED),
            ("América do Norte", "italic", MUTED),
        ],
        "note": "quem integra e mede em TLS",
        "hl": False,
    },
    {
        "kicker": "ANEL 3",
        "title": "Camada de token (JWT)",
        "body": [
            ("UFSC / LabSEC — Brasil", "bold", BODY),
            ("Custódio · Giron · Schardong", "normal", BODY),
            ("Alkhulaifi & El-Alfy · Kalpana", "normal", BODY),
        ],
        "note": "anel mais esparso — a lacuna do TCC",
        "hl": True,
    },
]

for x0, c in zip(X0, cards):
    usable = CARD_W - 2 * PAD
    box = FancyBboxPatch(
        (x0, CARD_Y0), CARD_W, CARD_Y1 - CARD_Y0,
        boxstyle="round,pad=0,rounding_size=0.22",
        facecolor=CARD_BG,
        edgecolor=RED if c["hl"] else CARD_EDGE,
        linewidth=1.6 if c["hl"] else 0.8,
    )
    ax.add_patch(box)

    cx = x0 + PAD
    y = CARD_Y1 - 0.58
    text_fit(cx, y, c["kicker"], usable, 8, fontweight="bold", color=RED)
    y -= 0.60
    text_fit(cx, y, c["title"], usable, 10.5, fontweight="bold", color=INK)
    y -= 0.40
    ax.plot([cx, x0 + CARD_W - PAD], [y, y], color=CARD_EDGE, lw=0.8)
    y -= 0.50
    for text, style, color in c["body"]:
        text_fit(cx, y, text, usable, 9,
                 fontweight="bold" if style == "bold" else "normal",
                 fontstyle="italic" if style == "italic" else "normal",
                 color=color)
        y -= LINE

    text_fit(x0 + CARD_W / 2, 0.30, c["note"], CARD_W, 8,
             ha="center", fontstyle="italic", color=MUTED)

# bloco de destaque "ESTE TRABALHO" dentro do card 3
hx0 = X0[2] + 0.30
hw = CARD_W - 0.60
hb = FancyBboxPatch((hx0, CARD_Y0 + 0.28), hw, 1.42,
                    boxstyle="round,pad=0,rounding_size=0.16",
                    facecolor=RED, edgecolor="none")
ax.add_patch(hb)
text_fit(hx0 + hw / 2, CARD_Y0 + 0.28 + 1.00, "★ ESTE TRABALHO", hw - 0.3, 10.5,
         ha="center", fontweight="bold", color="white")
text_fit(hx0 + hw / 2, CARD_Y0 + 0.28 + 0.46, "JWT + benchmark de serviço", hw - 0.3, 8.5,
         ha="center", color="white")

# setas "fornece" entre os cards
mid_y = (CARD_Y0 + CARD_Y1) / 2
for i in range(2):
    a0 = X0[i] + CARD_W + 0.10
    a1 = X0[i + 1] - 0.10
    arrow = FancyArrowPatch((a0, mid_y), (a1, mid_y),
                            arrowstyle="-|>", mutation_scale=15,
                            color=RED, lw=2.0)
    ax.add_patch(arrow)
    text_fit((a0 + a1) / 2, mid_y + 0.36, "fornece", a1 - a0, 7.8,
             ha="center", fontstyle="italic", color=MUTED)

out = "/private/tmp/claude-502/-Users-Marcelo-Petroni-Documents-FastAPI/171cb5ca-5a52-46cf-9413-521d520bf9fc/scratchpad/mapa_area.png"
fig.savefig(out, dpi=300, facecolor="white")
print("saved", out)
