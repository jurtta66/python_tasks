import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
import random as r
import math

  
def gen_points(n):
    np.random.seed()
    points = []
    for i in range(n):
        points.append((round(r.uniform(0, math.pi), 3), round(r.uniform(0, 1), 3)))
    return points

points = gen_points(1000000)


N = sum([i[1] for i in points])


def mc(i):
    if i[1] <= math.sin(i[0]):
        return i[1]
    else: return 0


if __name__ == '__main__':
    with Pool(4) as p:
        M = sum(p.map(mc, points))
        print(N/M)
    


    
