from solvers.fenics_2d_export import run_fisher_kpp_2d
import numpy as np
import pandas as pd
import os

def generate_param_grid(D_vals, r_vals, K_vals):
    for D in D_vals:
        for r in r_vals:
            for K in K_vals:
                yield D, r, K

def run_batch_simulations(output_dir="data/cnn_2d"):
    os.makedirs(output_dir, exist_ok=True)
    params = []
    i = 0
    for D, r, K in generate_param_grid([1e-6, 2e-6], [0.1, 0.2], [1.0, 1.5]):
        csv_path = os.path.join(output_dir, f"sim_{i}.csv")
        mesh, V, results = run_fisher_kpp_2d(D, r, K, T=5.0, steps=50, mesh_size=32, export_path=csv_path)
        params.append({"index": i, "D": D, "r": r, "K": K})
        i += 1

    pd.DataFrame(params).to_csv(os.path.join(output_dir, "labels.csv"), index=False)