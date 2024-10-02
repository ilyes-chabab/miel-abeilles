import tkinter as tk
from tkinter import ttk
from hive import Hive, BEEHIVE_POS, POPULATION_SIZE
import matplotlib.pyplot as plt

class BeeSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bee Simulation")

        self.population_rate = tk.DoubleVar(value=0.2)
        self.mutate_rate = tk.DoubleVar(value=0.045)
        self.num_generations = tk.IntVar(value=1500)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Population Rate:").grid(column=0, row=0, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.population_rate).grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(self.root, text="Mutate Rate:").grid(column=0, row=1, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.mutate_rate).grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Generations:").grid(column=0, row=2, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.num_generations).grid(column=1, row=2, padx=10, pady=5)

        ttk.Button(self.root, text="Run Simulation", command=self.run_simulation).grid(column=0, row=3, columnspan=2, pady=10)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(column=0, row=4, columnspan=2, pady=10)

    def run_simulation(self):
        self.progress["maximum"] = self.num_generations.get()
        self.progress["value"] = 0

        hive = Hive()
        generation = 0
        best_distance = hive.best_bee.distance
        best_distances = [best_distance]

        while generation < self.num_generations.get():
            hive.select_and_breed()
            generation += 1
            if hive.best_bee.distance < best_distance:
                best_distance = hive.best_bee.distance
            best_distances.append(hive.best_bee.distance)
            self.progress["value"] = generation
            self.root.update_idletasks()

        self.plot_field(hive.best_bee.flowers, BEEHIVE_POS)
        self.plot_best_path(hive.best_bee, BEEHIVE_POS, generation, best_distance, hive.total_mutations, hive.total_bees_generated)
        self.plot_best_distances(best_distances, self.mutate_rate.get(), 1 - self.mutate_rate.get(), POPULATION_SIZE)

    def plot_field(self, flowers, BEEHIVE_POS):
        x, y = zip(*flowers)
        plt.scatter(x, y, c="blue", label="Flowers")
        plt.scatter(*BEEHIVE_POS, c="red", label="Hive")
        plt.title("Field")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()

    def plot_best_distances(self, best_distances, mutate_rate, crossover_rate, population_size):
        plt.plot(best_distances)
        plt.title("Best Distance per Generation")
        plt.xlabel("Generation")
        plt.ylabel("Best Distance")
        textstr = "   ".join(
            (
                f"Mutation Rate: {mutate_rate * 100:.2f}%",
                f"Crossover Rate: {crossover_rate * 100:.2f}%",
                f"Population Size: {population_size}",
            )
        )

        plt.figtext(
            0.5,
            0.95,
            textstr,
            fontsize=8,
            ha="center",
            bbox=dict(facecolor="white", alpha=0.5),
        )

        plt.show()

    def plot_best_path(self, best_bee, BEEHIVE_POS, generation, best_distance, total_mutations, total_bees_generated):
        path = [BEEHIVE_POS] + best_bee.path + [BEEHIVE_POS]
        x, y = zip(*path)
        plt.plot(x, y, marker="o")
        plt.scatter(*BEEHIVE_POS, c="red", label="Hive", zorder=5)
        plt.title("Best path found")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        textstr = "   ".join(
            (
                f"Generations: {generation}",
                f"Best distance: {best_distance:.2f}",
                f"Total mutations: {total_mutations}",
                f"Total bees generated: {total_bees_generated}",
                f"Population size: {POPULATION_SIZE}",
                f"Mutate rate: {self.mutate_rate.get() * 100:.2f}%",
                f"Best population rate: {self.population_rate.get() * 100:.2f}%",
            )
        )
        plt.figtext(
            0.5,
            0.95,
            textstr,
            fontsize=8,
            ha="center",
            bbox=dict(facecolor="white", alpha=0.5),
        )

        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BeeSimulationApp(root)
    root.mainloop()
