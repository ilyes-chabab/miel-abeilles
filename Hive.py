import pandas as pd 
import random


class Bee:

    def __init__(self) :
        
        self.flowers = self.get_distance()

    def get_flower_pos(self):
        df = pd.read_excel('Champ de pissenlits et de sauge des pres.xlsx')
        flowers = []
        for i in range(len(df)) :
            flowers.append((df['x'][i] ,df["y"][i])  )
        path = random.sample(self.get_flower_pos())
        return path

    def get_distance(self):
        self.distance = random.randint(0,400)
        return self.distance
        

class Hive:

    def __init__(self) :
        self.bee =  Bee()
        self.distance = self.bee.get_distance()
    
    def get_distance(self):
        return self.distance

bee = Bee() 
hive = Hive()
print(hive.get_distance())