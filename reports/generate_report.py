from jinja2 import Template
import markdown2
import pdfkit

def create_markdown_report(sim_info, image_path, output_md="reports/sim_report.md"):
    template = Template("""
# Reporte de Simulación Fisher-KPP 2D

**Parámetros:**

- Difusión: {{ D }}
- Crecimiento: {{ r }}
- Capacidad: {{ K }}

**Resultado final:**

![Distribución final](../{{ image_path }})

""")
    md_content = template.render(**sim_info)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
    return output_md

def export_pdf_from_md(md_path, output_pdf="reports/sim_report.pdf"):
    html = markdown2.markdown_path(md_path)
    pdfkit.from_string(html, output_pdf)
