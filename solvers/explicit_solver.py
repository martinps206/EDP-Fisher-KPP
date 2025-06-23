import numpy as np

def solve_fisher_kpp(D, r, K, L, T, Nx, Nt):
    dx = L / (Nx - 1)
    dt = T / Nt
    x = np.linspace(0, L, Nx)
    u = np.exp(-100 * (x - L/2)**2)  # campana gaussiana

    alpha = D * dt / dx**2
    if alpha > 0.5:
        print(f"[⚠️] Instabilidad numérica: alpha = {alpha:.2f}")

    U = [u.copy()]
    for n in range(Nt):
        u_new = u.copy()
        for i in range(1, Nx - 1):
            diffusion = alpha * (u[i+1] - 2*u[i] + u[i-1])
            reaction = dt * r * u[i] * (1 - u[i]/K)
            u_new[i] += diffusion + reaction
        U.append(u_new.copy())
        u = u_new
    return x, U