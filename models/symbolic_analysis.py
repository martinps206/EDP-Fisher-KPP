import sympy as sp

def fisher_kpp_symbolic():
    x, t, D, r, K = sp.symbols('x t D r K')
    u = sp.Function('u')(x, t)
    
    eq = sp.Eq(sp.Derivative(u, t), D*sp.Derivative(u, x, 2) + r*u*(1 - u/K))
    return eq

# Visualización del análisis
if __name__ == "__main__":
    eq = fisher_kpp_symbolic()
    sp.pprint(eq)