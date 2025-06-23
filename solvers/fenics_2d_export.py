from fenics import *
import numpy as np
import pandas as pd

def run_fisher_kpp_2d(D=1e-6, r=0.2, K=1.0, T=5.0, steps=50, mesh_size=64, export_path=None):
    mesh = UnitSquareMesh(mesh_size, mesh_size)
    V = FunctionSpace(mesh, "P", 1)

    u_0_expr = Expression("exp(-100*(pow(x[0]-0.5,2) + pow(x[1]-0.5,2)))", degree=2)
    u_n = interpolate(u_0_expr, V)

    u = TrialFunction(V)
    v = TestFunction(V)
    dt = T / steps

    F = u*v*dx + dt*D*dot(grad(u), grad(v))*dx - (u_n + dt*r*u_n*(1 - u_n/K))*v*dx
    a, L = lhs(F), rhs(F)

    u_sol = Function(V)
    results = []
    times = []

    for n in range(steps):
        solve(a == L, u_sol)
        results.append(u_sol.copy(deepcopy=True))
        times.append(n * dt)
        u_n.assign(u_sol)

    # Exportación como dataset
    if export_path:
        export_to_csv(results, mesh, V, times, export_path)

    return mesh, V, results


def export_to_csv(results, mesh, V, times, output_csv):
    coordinates = mesh.coordinates()
    data = []

    for t_idx, u in enumerate(results):
        for i, (x, y) in enumerate(coordinates):
            u_val = u(Point(x, y))
            data.append([times[t_idx], x, y, u_val])

    df = pd.DataFrame(data, columns=["t", "x", "y", "u"])
    df.to_csv(output_csv, index=False)
