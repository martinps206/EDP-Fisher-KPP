import numpy as np
import pandas as pd
import os

def save_to_csv(x, U, path="data/solution.csv"):
    df = pd.DataFrame(U, columns=[f"x={xi:.3f}" for xi in x])
    df.insert(0, "time_step", range(len(U)))
    df.to_csv(path, index=False)

def save_to_parquet(x, U, path="data/solution.parquet"):
    df = pd.DataFrame(U, columns=[f"x={xi:.3f}" for xi in x])
    df.insert(0, "time_step", range(len(U)))
    df.to_parquet(path, index=False)

def export_simulation(x, U, path_csv="data/epidemic_simulation.csv", path_parquet="data/epidemic_simulation.parquet"):
    df = pd.DataFrame(U, columns=[f"x={xi:.4f}" for xi in x])
    df.insert(0, "time_step", range(len(U)))
    df.to_csv(path_csv, index=False)
    df.to_parquet(path_parquet, index=False)
    return df