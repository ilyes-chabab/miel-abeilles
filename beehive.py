import pandas as pd
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

        self.flowers = init_flowers_list()
        self.start = (500, 500)
        self.mutate_rate = 0.2
        self.build_random_path()
        self.distance = 0


    def build_random_path(self):
        self.path = random.sample(self.flowers, len(self.flowers))
        return self.path

    def compute_distance(self):
        '''
        path = path that the bee will travel
        self.distance = the entire distance that the bee will travel

        the loop  will calculate the distance ( thanks to pythagorean theorem) between two flowers and add the sum to 
        self.distance

        
        '''
        
        
        actual_pos = self.start #(500,500)
        for flower in self.path:
            # theoreme of pythagore to know the distance between 2 flowers
            self.distance += math.sqrt(((actual_pos[0] - flower[0]) ** 2)+ ((actual_pos[1] - flower[1]) ** 2))
            actual_pos = (flower[0], flower[1])
        #calculate the distance between the last pos and the start pos (the bee back to the hive)
        self.distance += math.sqrt(((actual_pos[0] - self.start[0]) ** 2)+ ((actual_pos[1] - self.start[1]) ** 2))
        return self.distance

    def mutate(self):
        pass


if __name__ == "__main__":
    bee = Bee()
    distance = bee.compute_distance()
    print(distance)
