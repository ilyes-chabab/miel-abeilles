import random
import math

BEEHIVE_POS = (500, 500)  # The position of the beehive
MUTATE_RATE = 0.045  # The probability of a bee to mutate
POPULATION_SIZE = 100  # The size of the population of bees
POPULATION_RATE = 0.2  # The rate of the population to select for the next generation
# random.seed(42)  # Uncomment this line to get the same results every time


def init_flowers_list():  # Read the flowers from the file and return a list of positions
    with open("field.txt", "r") as file:
        lines = file.readlines()
    pos = []
    for line in lines[1:]:
        values = line.strip().split()
        pos.append(((int(values[0])), (int(values[1]))))
    return pos


FLOWERS = init_flowers_list()  # The list of flowers the bees have to collect


class Bee:  # The bee class represents a bee that has a path to follow and a distance to the flowers
    def __init__(self):
        self.flowers = FLOWERS
        self.build_random_path()
        self.calculate_fitness()

    def build_random_path(self):  # Build a random path to the flowers
        self.path = random.sample(self.flowers, len(self.flowers))

    def calculate_fitness(
        self,
    ):  # Calculate the distance of the path the bee has to follow to collect all the flowers and return to the beehive
        self.distance = 0
        actual_pos = BEEHIVE_POS
        for flower in self.path:
            self.distance += math.sqrt(
                ((actual_pos[0] - flower[0]) ** 2) + ((actual_pos[1] - flower[1]) ** 2)
            )
            actual_pos = (flower[0], flower[1])
        self.distance += math.sqrt(
            ((actual_pos[0] - BEEHIVE_POS[0]) ** 2)
            + ((actual_pos[1] - BEEHIVE_POS[1]) ** 2)
        )

    def mutate(
        self, paths
    ):  # Mutate the path of the bee by swapping two random flowers
        nb_of_pos_mutated = max(1, int(len(paths) * MUTATE_RATE))
        pos_mutate = random.sample(range(len(paths)), nb_of_pos_mutated)
        for i in range(0, len(pos_mutate) - 1, 2):
            id, id2 = pos_mutate[i], pos_mutate[i + 1]
            paths[id], paths[id2] = paths[id2], paths[id]
        return paths

    def crossover(self, other_bee):  # Crossover the path of the bee with another bee
        cut = random.randint(0, len(self.path) - 1)
        new_path = self.path[:cut] + [
            flower for flower in other_bee.path if flower not in self.path[:cut]
        ]
        return new_path


class Hive:
    def __init__(self):
        self.population = [Bee() for _ in range(POPULATION_SIZE)]
        self.best_bee = None
        self.evaluate_population()
        self.total_mutations = 0
        self.total_bees_generated = POPULATION_SIZE

    def evaluate_population(
        self,
    ):  # Evaluate the population of bees and sort them by distance
        self.population.sort(key=lambda bee: bee.distance)
        self.best_bee = self.population[0]

    def select_best_bees(self):  # Select the best bees of the population
        selected_bees_count = int(len(self.population) * POPULATION_RATE)
        return self.population[:selected_bees_count]

    def create_mutated_bee(
        self, selected_bee
    ):  # Create a mutated bee from a selected bee
        new_bee = Bee()
        new_bee.path = selected_bee.mutate(selected_bee.path)
        new_bee.calculate_fitness()
        self.total_mutations += 1
        return new_bee

    def create_crossover_bee(
        self, parent1, parent2
    ):  # Create a bee from two parents by crossover
        new_bee = Bee()
        new_bee.path = parent1.crossover(parent2)
        new_bee.calculate_fitness()
        return new_bee

    def generate_new_population(
        self, selected_bees
    ):  # Generate a new population of bees from the selected bees
        new_population = []  # Keep the elite bees for the next generation
        while (
            len(new_population) < POPULATION_SIZE
        ):  # Generate new bees by mutation or crossover
            if (
                random.random() < MUTATE_RATE
            ):  # Mutate the bee with a probability of MUTATE_RATE
                parent = random.choice(selected_bees)
                new_bee = self.create_mutated_bee(parent)
            else:  # Crossover two random selected bees
                parent1, parent2 = random.sample(selected_bees, 2)
                new_bee = self.create_crossover_bee(parent1, parent2)
            new_population.append(new_bee)
            self.total_bees_generated += 1
        return new_population

    def select_and_breed(
        self,
    ):  # Select the best bees of the population and generate a new population from them
        selected_bees = self.select_best_bees()
        self.population = self.generate_new_population(selected_bees)
        self.evaluate_population()
