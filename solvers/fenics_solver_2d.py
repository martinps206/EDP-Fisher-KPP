from fenics import *
import numpy as np

def fisher_kpp_fenics_2d(D=1e-6, r=0.2, K=1.0, T=5.0, num_steps=50, mesh_size=64):
    mesh = UnitSquareMesh(mesh_size, mesh_size)
    V = FunctionSpace(mesh, 'P', 1)

    # Condición inicial
    u_0_expr = Expression('exp(-100 * pow(x[0]-0.5, 2) - 100 * pow(x[1]-0.5, 2))', degree=2)
    u_n = interpolate(u_0_expr, V)

    u = TrialFunction(V)
    v = TestFunction(V)
    dt = T / num_steps

    # Forma débil
    F = u*v*dx + dt*D*dot(grad(u), grad(v))*dx - (u_n + dt*r*u_n*(1 - u_n/K))*v*dx
    a, L = lhs(F), rhs(F)

    u_sol = Function(V)
    results = []

    for n in range(num_steps):
        solve(a == L, u_sol)
        results.append(u_sol.copy(deepcopy=True))
        u_n.assign(u_sol)

    return mesh, results