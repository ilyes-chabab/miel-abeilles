import random
import math

START = (500, 500)
MUTATE_RATE = 0.2
POPULATION_SIZE = 100

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

    def mutate(self, paths): # Mutate the path by swapping two random positions 
        nb_of_pos_mutated = len(paths) * MUTATE_RATE
        pos_mutate = random.sample(range(len(paths)), int(nb_of_pos_mutated))
        for id in range(0, len(pos_mutate), 2):
            id, id2 = pos_mutate[id], pos_mutate[id + 1]
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

    def select_and_breed(self): # Select the best bees and breed them to create a new population 
        selected_bees = self.population[:POPULATION_SIZE // 2] # Select the best half of the population 
        new_population = [] # Create a new population 

        for bee in selected_bees: # For each selected bee, create a new bee by mutating its path 
            new_bee = Bee()
            new_bee.path = bee.mutate(bee.path)
            new_bee.calculate_fitness()
            new_population.append(new_bee)
            self.total_mutations += 1

        while len(new_population) < POPULATION_SIZE: # Fill the rest of the population with new bees 
            new_population.append(Bee())
            self.total_bees_generated += 1

        self.population = new_population # Replace the old population with the new one 
        self.evaluate_population() # Evaluate the new population 

