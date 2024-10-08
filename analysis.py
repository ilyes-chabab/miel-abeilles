import time
import itertools
import matplotlib.pyplot as plt
from beehive import Hive
from config import POPULATION_RATES, MUTATION_INTENSITIES, MUTATE_RATES, GENERATIONS


def run_simulation(population_rate, mutation_intensity, mutate_rate, generations):
    hive = Hive(
        population_rate=population_rate,
        mutation_intensity=mutation_intensity,
        mutate_rate=mutate_rate,
    )
    for generation in range(generations):
        hive.select_and_breed()
    return hive.best_bee.distance


def analyze_parameters(
    population_rates, mutation_intensities, mutate_rates, generations
):
    results = []
    total_combinations = (
        len(population_rates) * len(mutation_intensities) * len(mutate_rates)
    )

    for i, (population_rate, mutation_intensity, mutate_rate) in enumerate(
        itertools.product(population_rates, mutation_intensities, mutate_rates)
    ):
        start_time = time.time()
        distance = run_simulation(
            population_rate, mutation_intensity, mutate_rate, generations
        )
        execution_time = time.time() - start_time
        results.append(
            (population_rate, mutation_intensity, mutate_rate, distance, execution_time)
        )

        # Print the progress
        print(f"Analyzing combination {i + 1}/{total_combinations}...")

    print("Analysis complete!")  # Message indiquant la fin de l'analyse
    return results


def plot_results(results):
    distances = [result[3] for result in results]
    population_rates = [result[0] for result in results]
    mutation_intensities = [result[1] for result in results]
    mutate_rates = [result[2] for result in results]

    plt.figure(figsize=(12, 6))
    plt.scatter(population_rates, distances, alpha=0.7)
    plt.title("Distance Found vs Population Rate", fontsize=16)
    plt.xlabel("Population Rate", fontsize=14)
    plt.ylabel("Distance Found", fontsize=14)
    plt.grid()
    plt.tight_layout()

    plt.figure(figsize=(12, 6))
    plt.scatter(mutation_intensities, distances, alpha=0.7)
    plt.title("Distance Found vs Mutation Intensity", fontsize=16)
    plt.xlabel("Mutation Intensity", fontsize=14)
    plt.ylabel("Distance Found", fontsize=14)
    plt.grid()
    plt.tight_layout()

    plt.figure(figsize=(12, 6))
    plt.scatter(mutate_rates, distances, alpha=0.7)
    plt.title("Distance Found vs Mutation Rate", fontsize=16)
    plt.xlabel("Mutation Rate", fontsize=14)
    plt.ylabel("Distance Found", fontsize=14)
    plt.grid()
    plt.tight_layout()

    plt.show()
