import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from models.exporter import export_simulation

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from solvers.explicit_solver import solve_fisher_kpp  # <- ahora se encuentra

st.title("Simulación de propagación con el modelo Fisher-KPP")

D = st.slider("Coeficiente de difusión (D)", 1e-7, 1e-5, 1e-6, format="%.1e")
r = st.slider("Tasa de crecimiento (r)", 0.01, 1.0, 0.2)
K = st.slider("Capacidad de carga (K)", 0.1, 2.0, 1.0)
T = st.slider("Tiempo total (T)", 1.0, 20.0, 10.0)
Nx = st.slider("Resolución espacial (Nx)", 50, 200, 100)

x, U = solve_fisher_kpp(D, r, K, L=1.0, T=T, Nx=Nx, Nt=1000)

step = st.slider("Paso de tiempo a visualizar", 0, len(U)-1, 0)
fig, ax = plt.subplots()
ax.plot(x, U[step])
ax.set_title(f"Solución en t = {T*step/1000:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("u(x, t)")
st.pyplot(fig)


if st.button("📤 Exportar resultados"):
    df = export_simulation(x, U)
    st.success("Simulación exportada con éxito.")
    st.dataframe(df.head())
    st.download_button("⬇️ Descargar CSV", data=df.to_csv(index=False), file_name="simulacion.csv")

# Validación visual del alpha
dx = 1.0 / (Nx - 1)
dt = T / 1000
alpha = D * dt / dx**2
if alpha > 0.5:
    st.error(f"⚠️ Condición de estabilidad violada: alpha = {alpha:.3f} > 0.5")
else:
    st.info(f"✅ Estable numéricamente: alpha = {alpha:.3f}")