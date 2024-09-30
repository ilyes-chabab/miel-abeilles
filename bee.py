import random
import math



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

        self.flowers = FLOWERS
        self.build_random_path()
        self.calculate_fitness()

    def build_random_path(self):
        self.path = random.sample(self.flowers, len(self.flowers))

    def calculate_fitness(self):
        """
        path = path that the bee will travel
        self.distance = the entire distance that the bee will travel

        the loop  will calculate the distance ( thanks to pythagorean theorem) between two flowers and add the sum to
        self.distance


        """
        self.distance = 0
        actual_pos = BEEHIVE_POS  # (500,500)
        for flower in self.path:
            # theoreme of pythagore to know the distance between 2 flowers
            self.distance += math.sqrt(((actual_pos[0] - flower[0]) ** 2) + ((actual_pos[1] - flower[1]) ** 2))
            actual_pos = (flower[0], flower[1])
        # calculate the distance between the last pos and the start pos (the bee back to the hive)
        self.distance += math.sqrt(((actual_pos[0] - BEEHIVE_POS[0]) ** 2) + ((actual_pos[1] - BEEHIVE_POS[1]) ** 2))

    def mutate(self):
        nb_of_pos_mutated = len(self.path) * MUTATE_RATE
        pos_mutate = random.sample(range(len(self.path)), int(nb_of_pos_mutated))
        
        for id in range(0, len(pos_mutate), 2):
            id, id2 = pos_mutate[id], pos_mutate[id + 1]
            self.path[id], self.path[id2] = self.path[id2], self.path[id]

if __name__ == "__main__":
    BEEHIVE_POS = (500, 500)
    MUTATE_RATE = 0.2
    FLOWERS = init_flowers_list()
    bee = Bee()
    distance = bee.distance
    path = bee.path
    print("distance : ", distance, "path : ", path)
    bee.path = bee.mutate()
    print(bee.path)
