from solvers.explicit_solver import solve_fisher_kpp
from models.exporter import export_simulation
import pandas as pd

results = []
for D in [1e-6, 2e-6]:
    for r in [0.1, 0.2]:
        for K in [1.0, 1.5]:
            x, U = solve_fisher_kpp(D, r, K, 1.0, 10.0, 100, 1000)
            final = U[-1]
            avg = sum(final)/len(final)
            results.append({"D": D, "r": r, "K": K, "u_avg_final": avg})

df = pd.DataFrame(results)
df.to_csv("data/ml_regression_dataset.csv", index=False)