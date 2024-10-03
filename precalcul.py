from beehive import FLOWERS
import math

def precalcul_distances():
    distances = []
    positions =[]
    positions.append(FLOWERS)
    positions[0].append((500,500))
    print(positions)
    for i in range(len(FLOWERS)):
        for j in range(len(FLOWERS)):
            if  FLOWERS[i] != FLOWERS[j]:
                x1 = FLOWERS[i][0]
                x2 = FLOWERS[i][1]
                y1 = FLOWERS[j][0]
                y2 = FLOWERS[j][1]
                result = math.sqrt(((x1-y1)**2) + ((x2-y2)**2))
                distances.append([FLOWERS[i],FLOWERS[j],result])
    
    
    with open('distances.txt', 'w') as file:
        for x,y,dist in distances:
            file.write(f"{x}\t{y}\t{dist}\n")
    

if __name__ == "__main__":
    precalcul_distances()
