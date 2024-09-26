import pandas as pd 
import random

def init_flowers_list():

    with open ("field.txt" , "r") as file :
        lines = file.readlines()
    pos = []

    for line in lines[1:] :
       
        values = line.strip().split()
        
        pos.append(((int(values[0])), (int(values[1]))))
    
    return pos

class Bee:

    def __init__(self) :
        
        self.flowers = init_flowers_list()
        self.start = (500,500)

    def get_flower_pos(self):
        path = random.sample(self.flowers, len(self.flowers))
        return path

    def get_distance(self):
        import math
        path = self.get_flower_pos()
        path.append(self.start)

        compute_path = 0
        actual_pos = (self.start)
        for flowers in path:
            # theoreme of pythagore to know the distance between 2 flowers
            compute_path += (math.sqrt(((actual_pos[0] - flowers[0])**2) + ((actual_pos[1] - flowers[1])**2)))
            actual_pos = (flowers[0],flowers[1])

        distance = compute_path
        print(distance)
        return distance
        

class Hive:

    def __init__(self) :
        self.bee_number = 100
        self.bee =  Bee()
        self.distance = self.bee.get_distance()
    
    def get_distance(self):
        return self.distance

    def get_all_bee_pos(self):
        for _ in range(self.bee_number):
            self.bee =  Bee()
            print(self.bee.get_distance())




if __name__ == "__main__":
    bee = Bee() 
    hive = Hive()
    # print(hive.get_all_bee_pos())
    # print(bee.get_distance())