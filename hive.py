import random
import math

BEEHIVE_POS = (500, 500)
MUTATE_RATE = 0.2
POPULATION_SIZE = 100
POPULATION_RATE = 0.1

# random.seed(42) # Uncomment this line to get the same results every time

def init_flowers_list(): # Read the flowers from the file and return a list of positions
    with open("field.txt", "r") as file:
        lines = file.readlines()
    pos = []
    for line in lines[1:]:
        values = line.strip().split()
        pos.append(((int(values[0])), (int(values[1]))))
    return pos

class Bee: # The bee class represents a bee that has a path to follow and a distance to the flowers 
    def __init__(self):
        self.flowers = init_flowers_list()
        self.build_random_path()
        self.calculate_fitness()

    def build_random_path(self): # Build a random path to the flowers 
        self.path = random.sample(self.flowers, len(self.flowers))
        return self.path

    def calculate_fitness(self): # Calculate the distance of the path 
        self.distance = 0
        actual_pos = BEEHIVE_POS
        for flower in self.path:
            self.distance += math.sqrt(
                ((actual_pos[0] - flower[0]) ** 2) + ((actual_pos[1] - flower[1]) ** 2)
            )
            actual_pos = (flower[0], flower[1])
        self.distance += math.sqrt(
            ((actual_pos[0] - BEEHIVE_POS[0]) ** 2) + ((actual_pos[1] - BEEHIVE_POS[1]) ** 2)
        )
        return self.distance

    def mutate(self, paths): # Mutate the path by swapping two random positions 
        nb_of_pos_mutated = int(len(paths) * MUTATE_RATE) 
        pos_mutate = random.sample(range(len(paths)), nb_of_pos_mutated)
        for i in range(0, len(pos_mutate) - 1, 2):
            id, id2 = pos_mutate[i], pos_mutate[i + 1]
            paths[id], paths[id2] = paths[id2], paths[id]
        return paths


class Hive: # The hive class contains the population of bees and the logic to evolve them 
    def __init__(self):
        self.population = [Bee() for _ in range(POPULATION_SIZE)] 
        self.best_bee = None 
        self.evaluate_population()
        self.total_mutations = 0 
        self.total_bees_generated = POPULATION_SIZE 

    def evaluate_population(self): # Sort the population by distance 
        self.population.sort(key=lambda bee: bee.distance) # Ascending order 
        self.best_bee = self.population[0] # The best bee is the first one 

    def select_best_bees(self):
        selected_bees_count = int(len(self.population) * POPULATION_RATE)
        return self.population[:selected_bees_count]

    def create_mutated_bee(self, selected_bee):
        new_bee = Bee()
        new_bee.path = selected_bee.mutate(selected_bee.path)
        new_bee.calculate_fitness()
        self.total_mutations += 1
        return new_bee

    def generate_new_population(self, selected_bees):
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            for selected_bee in selected_bees:
                if len(new_population) < POPULATION_SIZE:
                    new_bee = self.create_mutated_bee(selected_bee)
                    new_population.append(new_bee)
                    self.total_bees_generated += 1 # Incrémenter ici
        return new_population


    def select_and_breed(self):
        selected_bees = self.select_best_bees()
        self.population = self.generate_new_population(selected_bees)
        self.evaluate_population()