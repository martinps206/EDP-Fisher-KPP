import markdown2
import pdfkit

def generar_reporte(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        html = markdown2.markdown(f.read())
    pdfkit.from_string(html, pdf_path)