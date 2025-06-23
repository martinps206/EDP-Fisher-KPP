from models.fisher_kpp import load_parameters
from solvers.explicit_solver import solve_fisher_kpp
from solvers.crank_nicolson import crank_nicolson_fisher
from visualizations.plot_results import plot_solution
from visualizations.animate_results import animate_solution
from models.exporter import save_to_csv, save_to_parquet

def main():
    model, space = load_parameters()
    
    x, U = crank_nicolson_fisher(
        D=model['D'], r=model['r'], K=model['K'],
        L=space['L'], T=space['T'], Nx=space['Nx'], Nt=space['Nt']
    )

    plot_solution(x, U, space['T'], space['Nt'])
    animate_solution(x, U, space['T'], space['Nt'], save_path="plots/epidemia_cn.mp4")
    save_to_csv(x, U)
    save_to_parquet(x, U)

if __name__ == "__main__":
    main()