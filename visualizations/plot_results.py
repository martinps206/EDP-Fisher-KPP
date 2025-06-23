import matplotlib.pyplot as plt

def plot_solution(x, U, T, Nt, times=[0, 200, 400, 600, 800, 999]):
    plt.figure(figsize=(10, 6))
    for i in times:
        plt.plot(x, U[i], label=f"t = {T*i/Nt:.2f}")
    plt.xlabel("Espacio (x)")
    plt.ylabel("u(x, t)")
    plt.title("Propagación de la población (Fisher-KPP)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()