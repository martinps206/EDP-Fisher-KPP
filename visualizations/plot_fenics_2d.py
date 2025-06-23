import matplotlib.pyplot as plt
from fenics import plot

def plot_fenics_solution(mesh, results, steps=[0, 10, 25, 49]):
    for i in steps:
        plt.figure()
        plot(results[i], title=f"Paso {i}")
        plt.show()