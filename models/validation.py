import numpy as np

def traveling_wave(x, t, c, D, r):
    """
    Solución analítica aproximada de una onda viajera
    """
    return 1 / (1 + np.exp((x - c*t)/np.sqrt(4*D/r)))