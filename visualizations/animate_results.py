import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_solution(x, U, T, Nt, save_path="plots/animation.mp4"):
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(0, max(max(u) for u in U))
    ax.set_xlabel("Espacio")
    ax.set_ylabel("u(x, t)")
    ax.set_title("Propagación de una epidemia - Fisher-KPP")

    def init():
        line.set_data([], [])
        return line,

    def update(i):
        line.set_data(x, U[i])
        ax.set_title(f"Tiempo t = {T*i/Nt:.2f}")
        return line,

    ani = animation.FuncAnimation(fig, update, frames=len(U), init_func=init, blit=True)
    ani.save(save_path, writer="ffmpeg", fps=30)
    plt.close()
