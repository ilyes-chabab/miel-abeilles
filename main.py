import matplotlib.pyplot as plt
from hive import Hive, START, POPULATION_SIZE, MUTATE_RATE

def plot_field(flowers, start): # Plot the field with the flowers and the hive 
    x, y = zip(*flowers)
    plt.scatter(x, y, c='blue', label='Flowers')
    plt.scatter(*start, c='red', label='Hive')
    plt.title('Field')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

def plot_best_path(best_bee, start, generation, best_distance, total_mutations, total_bees_generated): # Plot the best path found by the bees 
    path = best_bee.path + [start]
    x, y = zip(*path)
    plt.plot(x, y, marker='o')
    plt.scatter(*start, c='red', label='Hive', zorder=5)
    plt.title('Best path found')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

   
    textstr = ' '.join((
        f'Generations: {generation}',
        f'Best distance: {best_distance:.2f}',
        f'Total mutations: {total_mutations}',
        f'Total bees generated: {total_bees_generated}',
        f'Population size: {POPULATION_SIZE}',
        f'Mutate rate: {MUTATE_RATE}'
    ))
    plt.figtext(0.5, 0.95, textstr, fontsize=8, ha='center', bbox=dict(facecolor='white', alpha=0.5))

    plt.show()

def main(): # Main function to run the genetic algorithm 
    hive = Hive()
    generation = 0
    best_distance = hive.best_bee.distance

    while True: # Evolve the population until the best bee doesn't improve anymore 
        hive.select_and_breed()
        generation += 1
        if hive.best_bee.distance < best_distance:
            best_distance = hive.best_bee.distance
        else:
            break 
        print(f"Generation {generation}: Best distance = {hive.best_bee.distance}")

    print(f"Best path found after {generation} generations:", hive.best_bee.path)
    print(f"Total mutations: {hive.total_mutations}")
    print(f"Total bees generated: {hive.total_bees_generated}")

    plot_field(hive.best_bee.flowers, START) 
    plot_best_path(hive.best_bee, START, generation, best_distance, hive.total_mutations, hive.total_bees_generated)

if __name__ == "__main__": 
    main() 
