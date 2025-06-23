import numpy as np
from scipy.linalg import solve_banded

def crank_nicolson_fisher(D, r, K, L, T, Nx, Nt):
    dx = L / (Nx - 1)
    dt = T / Nt
    x = np.linspace(0, L, Nx)

    alpha = D * dt / (2 * dx**2)
    u = np.exp(-100 * (x - L/2)**2)  # condición inicial

    # Matriz tridiagonal para método implícito
    ab = np.zeros((3, Nx))
    ab[0, 1:] = -alpha
    ab[1, :] = 1 + 2 * alpha
    ab[2, :-1] = -alpha

    # Condiciones de frontera fijas
    ab[1, 0] = ab[1, -1] = 1
    ab[0, 1] = ab[2, -2] = 0

    U = [u.copy()]
    for _ in range(Nt):
        b = u + dt * r * u * (1 - u/K)
        b[0] = b[-1] = 0
        u = solve_banded((1, 1), ab, b)
        U.append(u.copy())

    return x, U