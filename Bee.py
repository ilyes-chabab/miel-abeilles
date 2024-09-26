import pandas as pd
import random


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


    def build_random_path(self):
        self.path = random.sample(self.flowers, len(self.flowers))
        return self.path
    
    def compute_segment(self,x,y):
        return x-y

    def get_distance(self):
        import math
        path = self.path
        computed_path = 0
        actual_pos = self.start
        for flowers in path:
            # theoreme of pythagore to know the distance between 2 flowers
            computed_path += math.sqrt(((actual_pos[0] - flowers[0]) ** 2)+ ((actual_pos[1] - flowers[1]) ** 2))
            actual_pos = (flowers[0], flowers[1])
        print(actual_pos)
        computed_path += math.sqrt(((actual_pos[0] - self.start[0]) ** 2)+ ((actual_pos[1] - self.start[1]) ** 2))
        distance = computed_path
        return distance

    def mutate(self):
        pass


if __name__ == "__main__":
    bee = Bee()
    distance = bee.get_distance()
    print(distance)
