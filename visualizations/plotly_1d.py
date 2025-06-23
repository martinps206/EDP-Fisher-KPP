import plotly.express as px
import pandas as pd

def plotly_surface(x, U, T):
    Nt = len(U) - 1
    df = pd.DataFrame(U, columns=[f"{xi:.4f}" for xi in x])
    df["t"] = [T * i / Nt for i in range(len(U))]
    df_melted = df.melt(id_vars="t", var_name="x", value_name="u")

    df_melted["x"] = df_melted["x"].astype(float)
    fig = px.density_heatmap(
        df_melted, x="x", y="t", z="u", nbinsx=100, nbinsy=100,
        color_continuous_scale="Viridis", title="Mapa de calor u(x, t)"
    )
    fig.update_layout(yaxis_title="Tiempo", xaxis_title="Espacio")
    return fig