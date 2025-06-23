# 🧠 Fisher-KPP Epidemic Model Simulator 2D

### Simulación Avanzada de Propagación de Brotes en Tejidos Biológicos + Machine Learning

---

## 📌 Descripción

Este proyecto implementa una plataforma completa basada en el modelo de Fisher-KPP (Kolmogorov–Petrovsky–Piskunov) para simular la **propagación de una epidemia en un tejido biológico**, utilizando:

- 🔬 **Ecuaciones en derivadas parciales no lineales** (EDP tipo difusión-reacción)
- 🧮 **FEniCS** para resolución numérica en 2D mediante elementos finitos
- 🧠 **Machine Learning** supervisado (regresión inversa, predicción)
- 📊 **Visualizaciones interactivas** con Plotly y Streamlit
- 📁 **Exportación de datasets sintéticos** para entrenamiento de CNNs
- 📄 **Generación automática de informes científicos** en PDF

---

## 🧪 Modelo Matemático

El modelo Fisher-KPP en 2D describe la evolución de la densidad poblacional/infecciosa \( u(x, y, t) \):

\[
\frac{\partial u}{\partial t} = D \nabla^2 u + r u \left(1 - \frac{u}{K} \right)
\]

- \( D \): coeficiente de difusión (propagación en el tejido)
- \( r \): tasa de crecimiento (reproducción del virus)
- \( K \): capacidad de carga (valor máximo de población/infección)

---

## 🏗️ Estructura del Proyecto

fisher_kpp_model/
├── config/ # Parámetros YAML
├── data/ # Simulaciones CSV, Parquet, imágenes
├── models/ # Modelo Fisher-KPP, exportador, simbólico (SymPy)
├── solvers/ # Solvers: explícito 1D, FEniCS 2D, Crank-Nicolson (futuro)
├── visualizations/ # Plotly, matplotlib
├── data_generation/ # Scripts de generación automática de datasets
├── dashboard/ # App interactiva con Streamlit
├── notebooks/ # Exploración ML, análisis de sensibilidad
├── reports/ # Informe automático Markdown → PDF
├── requirements.txt
└── README.md



---

## 🚀 Funcionalidades principales

### ✅ Simulación numérica:

- Simulación 1D (explícita) y 2D (FEniCS)
- Control de estabilidad con condición CFL
- Visualización de resultados en tiempo real

### ✅ Generación de datasets:

- Exportación a `.csv`, `.parquet`, `.npy` y `.png`
- Generación en lote de soluciones para entrenamiento de modelos ML
- Preprocesamiento para redes neuronales convolucionales

### ✅ Machine Learning:

- Regresión de \( u_{\text{final}} \) usando \( D, r, K \) como features
- ML inverso: estimar parámetros a partir de distribuciones
- Evaluación y métricas de error

### ✅ Visualizaciones:

- Plotly: 3D interactivo (`u(x, y, t)`)
- Animaciones, mapas de calor, curvas de convergencia
- Validación visual de errores numéricos

### ✅ Informes automáticos:

- Plantillas con Jinja2 y Markdown
- Exportación a PDF (gráficos incluidos)
- Útil para publicaciones o tesis

---

## 📦 Instalación

```bash
git clone https://github.com/tu_usuario/fisher-kpp-model.git
cd fisher-kpp-model
pip install -r requirements.txt
Para ejecutar FEniCS:

Recomendado: usar Docker FEniCS o un entorno Linux

Ejecución rápida
Simulación 1D con interfaz:

streamlit run dashboard/app.py
Simulación 2D y visualización:

streamlit run dashboard/fenics_2d_app.py

Machine Learning
Dataset de entrenamiento:

python data_generation/generate_2d_dataset.py
python data_generation/export_images.py
Entrenar regresor:

python notebooks/ml_regression_panel.py
📄 Generación de Informe PDF

from reports.generate_report import create_markdown_report, export_pdf_from_md

sim_info = {
  "D": 1e-6,
  "r": 0.2,
  "K": 1.0,
  "image_path": "data/images/img_0.png"
}

md_path = create_markdown_report(sim_info, sim_info["image_path"])
export_pdf_from_md(md_path)
🧰 Tecnologías
Python 3.11

FEniCS (solución de EDPs en 2D)

NumPy / Pandas / Matplotlib

Plotly / Streamlit

scikit-learn

SymPy

Jinja2 / markdown2 / pdfkit

🧰 Tecnologías
Python 3.11

FEniCS (solución de EDPs en 2D)

NumPy / Pandas / Matplotlib

Plotly / Streamlit

scikit-learn

SymPy

Jinja2 / markdown2 / pdfkit

📚 Créditos
Proyecto desarrollado por Martín Paliza Sánchez
Mentoría técnica y matemática por IA (OpenAI GPT-4o)

Este proyecto puede utilizarse como base para tesis, cursos de posgrado, papers científicos o aplicaciones docentes en bioingeniería, epidemiología computacional o matemática aplicada.