import random
import math

START = (500, 500)
MUTATE_RATE = 0.2
POPULATION_SIZE = 100
NO_IMPROVEMENT_LIMIT = 50 
def init_flowers_list():
    with open("field.txt", "r") as file:
        lines = file.readlines()
    pos = []
    for line in lines[1:]:
        values = line.strip().split()
        pos.append(((int(values[0])), (int(values[1]))))
    return pos

class Bee:
    def __init__(self):
        self.flowers = init_flowers_list()
        self.build_random_path()
        self.calculate_fitness()

    def build_random_path(self):
        self.path = random.sample(self.flowers, len(self.flowers))
        return self.path

    def calculate_fitness(self):
        self.distance = 0
        actual_pos = START
        for flower in self.path:
            self.distance += math.sqrt(
                ((actual_pos[0] - flower[0]) ** 2) + ((actual_pos[1] - flower[1]) ** 2)
            )
            actual_pos = (flower[0], flower[1])
        self.distance += math.sqrt(
            ((actual_pos[0] - START[0]) ** 2) + ((actual_pos[1] - START[1]) ** 2)
        )
        return self.distance

    def mutate(self, paths):
        nb_of_pos_mutated = len(paths) * MUTATE_RATE
        pos_mutate = random.sample(range(len(paths)), int(nb_of_pos_mutated))
        for id in range(0, len(pos_mutate), 2):
            id, id2 = pos_mutate[id], pos_mutate[id + 1]
            paths[id], paths[id2] = paths[id2], paths[id]
        return paths

class Hive:
    def __init__(self):
        self.population = [Bee() for _ in range(POPULATION_SIZE)]
        self.best_bee = None
        self.evaluate_population()
        self.total_mutations = 0
        self.total_bees_generated = POPULATION_SIZE

    def evaluate_population(self):
        self.population.sort(key=lambda bee: bee.distance)
        self.best_bee = self.population[0]

    def select_and_breed(self):
        selected_bees = self.population[:POPULATION_SIZE // 2]
        new_population = []

        for bee in selected_bees:
            new_bee = Bee()
            new_bee.path = bee.mutate(bee.path)
            new_bee.calculate_fitness()
            new_population.append(new_bee)
            self.total_mutations += 1

        while len(new_population) < POPULATION_SIZE:
            new_population.append(Bee())
            self.total_bees_generated += 1

        self.population = new_population
        self.evaluate_population()

if __name__ == "__main__":
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
