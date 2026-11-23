from pypdf import PdfReader, PdfWriter

tcc = PdfReader("TCC Gabriel Aragão.pdf")
ficha = PdfReader("fichaeletronica.pdf")
writer = PdfWriter()

posicao = 2  # inserir após a página 2 (folha de rosto), índice 0-based

for i, page in enumerate(tcc.pages):
    writer.add_page(page)
    if i == posicao - 1:
        for fp in ficha.pages:
            writer.add_page(fp)

with open("TCC_final.pdf", "wb") as f:
    writer.write(f)