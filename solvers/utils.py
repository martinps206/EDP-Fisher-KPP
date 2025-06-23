def compute_alpha(D, dt, dx):
    return D * dt / dx**2

def check_stability(alpha):
    return alpha < 0.5