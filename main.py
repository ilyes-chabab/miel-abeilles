import matplotlib.pyplot as plt
from hive import Hive, START, POPULATION_SIZE, MUTATE_RATE, NO_IMPROVEMENT_LIMIT

def plot_field(flowers, start):
    x, y = zip(*flowers)
    plt.scatter(x, y, c='blue', label='Fleurs')
    plt.scatter(*start, c='red', label='Ruche')
    plt.title('Champ de Fleurs')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

def plot_best_path(best_bee, start):
    path = best_bee.path + [start]
    x, y = zip(*path)
    plt.plot(x, y, marker='o')
    plt.scatter(*start, c='red', label='Ruche')
    plt.title('Meilleur Chemin Trouvé')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

def main():
    hive = Hive()
    generation = 0
    no_improvement_count = 0
    best_distance = hive.best_bee.distance

    while no_improvement_count < NO_IMPROVEMENT_LIMIT:
        hive.select_and_breed()
        generation += 1
        if hive.best_bee.distance < best_distance:
            best_distance = hive.best_bee.distance
            no_improvement_count = 0
        else:
            no_improvement_count += 1
        print(f"Generation {generation}: Best distance = {hive.best_bee.distance}")

    print(f"Best path found after {generation} generations:", hive.best_bee.path)
    print(f"Total mutations: {hive.total_mutations}")
    print(f"Total bees generated: {hive.total_bees_generated}")

    plot_field(hive.best_bee.flowers, START)
    plot_best_path(hive.best_bee, START)

if __name__ == "__main__":
    main()
