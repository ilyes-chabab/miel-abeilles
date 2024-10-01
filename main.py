import matplotlib.pyplot as plt
from hive import Hive, BEEHIVE_POS, POPULATION_SIZE, MUTATE_RATE, POPULATION_RATE,  ELITE_COUNT


def plot_field(flowers, BEEHIVE_POS): 
    x, y = zip(*flowers)
    plt.scatter(x, y, c="blue", label="Flowers")
    plt.scatter(*BEEHIVE_POS, c="red", label="Hive")
    plt.title("Field")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


def plot_best_distances(best_distances, mutate_rate, crossover_rate, population_size, elite_count):
    plt.plot(best_distances)
    plt.title("Best Distance per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    textstr = '   '.join((
        f"Mutation Rate: {mutate_rate * 100:.2f}%",
        f"Crossover Rate: {crossover_rate * 100:.2f}%",
        f"Population Size: {population_size}",
        f"Elite Count: {elite_count}",
    ))

    plt.figtext(0.5, 0.95, textstr, fontsize=8, ha='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()


def plot_best_path(
    best_bee,
    BEEHIVE_POS,
    generation,
    best_distance,
    total_mutations,
    total_bees_generated,
):  
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
            f"Mutate rate: {MUTATE_RATE}",
            f"Population rate: {POPULATION_RATE}",
            f"Elite count: {ELITE_COUNT}",
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


def main(num_generations):  
    hive = Hive()
    generation = 0
    best_distance = hive.best_bee.distance
    best_distances = [best_distance]

    while (
        generation < num_generations
    ):  
        hive.select_and_breed()
        generation += 1
        if hive.best_bee.distance < best_distance:
            best_distance = hive.best_bee.distance
        best_distances.append(
            hive.best_bee.distance
        )  
        print(f"Generation {generation}: Best distance = {hive.best_bee.distance}")

    print(f"Best path found after {generation} generations:", hive.best_bee.path)
    print(f"Total mutations: {hive.total_mutations}")
    print(f"Total bees generated: {hive.total_bees_generated}")

    plot_field(hive.best_bee.flowers, BEEHIVE_POS)
    plot_best_path(
        hive.best_bee,
        BEEHIVE_POS,
        generation,
        best_distance,
        hive.total_mutations,
        hive.total_bees_generated,
    )
    plot_best_distances(best_distances, MUTATE_RATE, 1 - MUTATE_RATE, POPULATION_SIZE, ELITE_COUNT)


if __name__ == "__main__":
    num_generations = 150  # Specify the number of generations you want to run
    main(num_generations)
