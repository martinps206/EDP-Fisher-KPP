import numpy as np

def compute_error(U1, U2):
    """
    Compara dos soluciones U1 y U2 (listas de vectores).
    Devuelve norma L2 promedio por paso de tiempo.
    """
    errors = []
    for u1, u2 in zip(U1, U2):
        error = np.linalg.norm(np.array(u1) - np.array(u2), ord=2)
        errors.append(error)
    return errors