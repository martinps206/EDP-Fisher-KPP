import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from solvers.fenics_2d_export import run_fisher_kpp_2d
import plotly.express as px
import pandas as pd

st.title("Simulación 2D Fisher-KPP con FEniCS")

D = st.slider("Difusión D", 1e-7, 1e-5, 1e-6, format="%.1e")
r = st.slider("Crecimiento r", 0.01, 1.0, 0.2)
K = st.slider("Capacidad K", 0.1, 2.0, 1.0)
steps = st.slider("Pasos de tiempo", 10, 100, 50)
mesh_size = st.slider("Tamaño de malla", 16, 64, 32)

export_path = "data/fenics_2d_dataset.csv"
if st.button("Ejecutar simulación"):
    mesh, V, results = run_fisher_kpp_2d(D, r, K, T=5.0, steps=steps, mesh_size=mesh_size, export_path=export_path)
    df = pd.read_csv(export_path)
    st.success(f"Dataset exportado a: {export_path}")
    step_selected = st.slider("Paso a mostrar", 0, steps-1, 0)
    df_t = df[df["t"] == df["t"].unique()[step_selected]]

    fig = px.scatter_3d(df_t, x="x", y="y", z="u", color="u", opacity=0.7,
                        title=f"Simulación en paso {step_selected}")
    st.plotly_chart(fig, use_container_width=True)
