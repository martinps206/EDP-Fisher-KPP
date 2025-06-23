import numpy as np

def solve_2d_fisher(D, r, K, L, T, Nx, Ny, Nt):
    dx = dy = L / (Nx - 1)
    dt = T / Nt
    alpha = D * dt / dx**2
    x = np.linspace(0, L, Nx)
    y = np.linspace(0, L, Ny)
    u = np.zeros((Nx, Ny))
    X, Y = np.meshgrid(x, y, indexing='ij')
    u = np.exp(-100 * ((X - L/2)**2 + (Y - L/2)**2))

    U = [u.copy()]
    for _ in range(Nt):
        u_new = u.copy()
        u_new[1:-1, 1:-1] += alpha * (
            u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4*u[1:-1, 1:-1]
        ) + dt * r * u[1:-1, 1:-1] * (1 - u[1:-1, 1:-1]/K)
        U.append(u_new.copy())
        u = u_new
    return X, Y, U