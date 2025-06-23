import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def csv_to_matrix(df):
    """Convierte df con columnas x,y,u a matriz 2D ordenada."""
    pivot = df.pivot(index="y", columns="x", values="u")
    matrix = pivot.sort_index(ascending=False).to_numpy()
    return matrix

def export_images(csv_folder="data/cnn_2d", image_folder="data/images"):
    os.makedirs(image_folder, exist_ok=True)
    labels = pd.read_csv(os.path.join(csv_folder, "labels.csv"))

    for idx in labels["index"]:
        df = pd.read_csv(os.path.join(csv_folder, f"sim_{idx}.csv"))
        final_t = df["t"].max()
        df_final = df[df["t"] == final_t]
        mat = csv_to_matrix(df_final)

        np.save(os.path.join(image_folder, f"img_{idx}.npy"), mat)
        plt.imsave(os.path.join(image_folder, f"img_{idx}.png"), mat, cmap="viridis")
