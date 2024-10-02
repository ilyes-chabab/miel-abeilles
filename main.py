import tkinter as tk
from tkinter import ttk
from hive import Hive, BEEHIVE_POS, POPULATION_SIZE, FLOWERS
import matplotlib.pyplot as plt


class BeeSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bee Simulation / Population size set at 100 bees")

        self.population_rate = tk.DoubleVar(value=0.2)
        self.mutate_rate = tk.DoubleVar(value=0.045)
        self.num_generations = tk.IntVar(value=1500)
        self.crossover_rate = tk.DoubleVar(value=1 - self.mutate_rate.get())
        self.MUTATION_INTENSITY = tk.DoubleVar(value=0.05)  # New variable

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Population Rate:").grid(
            column=0, row=0, padx=10, pady=5
        )
        ttk.Entry(self.root, textvariable=self.population_rate).grid(
            column=1, row=0, padx=10, pady=5
        )
        ttk.Label(
            self.root, text="Rate of the best bees selected for the next generations"
        ).grid(column=2, row=0, padx=10, pady=5)

        self.selected_bees_label = ttk.Label(self.root, text="")
        self.selected_bees_label.grid(column=0, row=1, columnspan=3, padx=10, pady=5)

        ttk.Label(self.root, text="Mutate Rate:").grid(column=0, row=2, padx=10, pady=5)
        ttk.Entry(self.root, textvariable=self.mutate_rate).grid(
            column=1, row=2, padx=10, pady=5
        )
        ttk.Label(self.root, text="Probability of a bee to mutate").grid(
            column=2, row=2, padx=10, pady=5
        )

        self.mutated_bees_label = ttk.Label(self.root, text="")
        self.mutated_bees_label.grid(column=0, row=3, columnspan=3, padx=10, pady=5)

        ttk.Label(self.root, text="Crossover Rate:").grid(
            column=0, row=4, padx=10, pady=5
        )
        ttk.Label(self.root, textvariable=self.crossover_rate).grid(
            column=1, row=4, padx=10, pady=5
        )
        ttk.Label(
            self.root, text="Probability of a bee interbreeding with another"
        ).grid(column=2, row=4, padx=10, pady=5)

        self.crossover_bees_label = ttk.Label(self.root, text="")
        self.crossover_bees_label.grid(column=0, row=5, columnspan=3, padx=10, pady=5)

        ttk.Label(self.root, text="Mutation intensity:").grid(
            column=0, row=6, padx=10, pady=5
        )
        ttk.Entry(self.root, textvariable=self.MUTATION_INTENSITY).grid(
            column=1, row=6, padx=10, pady=5
        )
        ttk.Label(
            self.root,
            text="Controls how many flower positions will be affected by the mutation",
        ).grid(column=2, row=6, padx=10, pady=5)

        self.mutated_positions_label = ttk.Label(self.root, text="")
        self.mutated_positions_label.grid(
            column=0, row=7, columnspan=3, padx=10, pady=5
        )

        ttk.Label(self.root, text="Number of Generations:").grid(
            column=0, row=8, padx=10, pady=5
        )
        ttk.Entry(self.root, textvariable=self.num_generations).grid(
            column=1, row=8, padx=10, pady=5
        )

        ttk.Button(self.root, text="Run Simulation", command=self.run_simulation).grid(
            column=0, row=9, columnspan=2, pady=10
        )

        self.progress = ttk.Progressbar(
            self.root, orient="horizontal", length=200, mode="determinate"
        )
        self.progress.grid(column=0, row=10, columnspan=2, pady=10)

        self.mutate_rate.trace("w", self.update_crossover_rate)
        self.mutate_rate.trace("w", self.update_mutated_bees_label)
        self.crossover_rate.trace("w", self.update_crossover_bees_label)
        self.MUTATION_INTENSITY.trace("w", self.update_mutated_positions_label)
        self.population_rate.trace("w", self.update_selected_bees_label)

        self.update_mutated_positions_label()
        self.update_selected_bees_label()
        self.update_mutated_bees_label()
        self.update_crossover_bees_label()

    def update_crossover_rate(self, *args):
        self.crossover_rate.set(1 - self.mutate_rate.get())

    def update_mutated_positions_label(self, *args):
        num_positions = max(1, int(len(FLOWERS) * self.MUTATION_INTENSITY.get()))
        self.mutated_positions_label.config(
            text=f"Number of flower positions changed: {num_positions} / 50"
        )

    def update_selected_bees_label(self, *args):
        num_selected_bees = max(1, int(POPULATION_SIZE * self.population_rate.get()))
        self.selected_bees_label.config(
            text=f"Number of best bees selected: {num_selected_bees} / 100"
        )

    def update_mutated_bees_label(self, *args):
        num_mutated_bees = int(POPULATION_SIZE * self.mutate_rate.get())
        self.mutated_bees_label.config(
            text=f"Number of bees mutated: {num_mutated_bees} / {POPULATION_SIZE}"
        )

    def update_crossover_bees_label(self, *args):
        num_crossover_bees = int(POPULATION_SIZE * self.crossover_rate.get())
        self.crossover_bees_label.config(
            text=f"Number of bees crossed over: {num_crossover_bees} / {POPULATION_SIZE}"
        )

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

        self.plot_field(FLOWERS, BEEHIVE_POS)
        self.plot_best_path(
            hive.best_bee,
            BEEHIVE_POS,
            generation,
            best_distance,
            hive.total_mutations,
            hive.total_bees_generated,
            self.crossover_rate.get(),
        )
        self.plot_best_distances(
            best_distances,
            self.mutate_rate.get(),
            self.crossover_rate.get(),
            POPULATION_SIZE,
            best_distance,
        )

    def plot_field(self, flowers, BEEHIVE_POS):
        x, y = zip(*flowers)
        plt.scatter(x, y, c="green", label="Flowers")
        plt.scatter(*BEEHIVE_POS, c="yellow", label="Hive")
        plt.title("Field")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()

    def plot_best_distances(
        self,
        best_distances,
        mutate_rate,
        crossover_rate,
        population_size,
        best_distance,
    ):
        plt.plot(best_distances)
        plt.title("Best Distance per Generation")
        plt.xlabel("Generation")
        plt.ylabel("Best Distance")
        textstr = "   ".join(
            (
                f"Mutation Rate: {mutate_rate * 100:.2f}%",
                f"Crossover Rate: {crossover_rate * 100:.2f}%",
                f"Population Size: {population_size}",
                f"Best Distance: {best_distance:.2f}",
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

    def plot_best_path(
        self,
        best_bee,
        BEEHIVE_POS,
        generation,
        best_distance,
        total_mutations,
        total_bees_generated,
        crossover_rate,
    ):
        path = [BEEHIVE_POS] + best_bee.path + [BEEHIVE_POS]
        x, y = zip(*path)
        plt.plot(x, y, marker="o")
        plt.scatter(*BEEHIVE_POS, c="yellow", label="Hive", zorder=5)
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
                f"Crossover rate: {crossover_rate * 100:.2f}%",
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
