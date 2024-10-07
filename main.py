import tkinter as tk
from bee_simulation_app import BeeSimulationApp
from analysis import analyze_parameters, plot_results
from config import POPULATION_RATES, MUTATION_INTENSITIES, MUTATE_RATES, GENERATIONS

def main():
    root = tk.Tk()
    app = BeeSimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    choice = input("Type 'gui' to run the GUI or 'analyze' to run the analysis: ").strip().lower()
    if choice == 'gui':
        main()
    elif choice == 'analyze':
        results = analyze_parameters(POPULATION_RATES, MUTATION_INTENSITIES, MUTATE_RATES, GENERATIONS)
        plot_results(results)
    else:
        print("Invalid choice. Please type 'gui' or 'analyze'.")
