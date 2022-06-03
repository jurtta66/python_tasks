# Метод Монте Карло.
from datetime import datetime
from numba import njit
import random as r
import math

def monte_carlo(n):
    points = []
    for i in range(n):
        points.append((round(r.uniform(0, math.pi), 3), round(r.uniform(0, 1), 3)))
    N = sum([i[1] for i in points]) 
    M = 0
    for i in points:
        if i[1] <= math.sin(i[0]):
            M += i[1]
    if M!=0: return round(N/M, 2)   

@njit
def monte_carlo_jit(n):
    points = []
    for i in range(n):
        points.append((round(r.uniform(0, math.pi), 3), round(r.uniform(0, 1), 3)))
    N = sum([i[1] for i in points]) 
    M = 0
    for i in points:
        if i[1] <= math.sin(i[0]):
            M += i[1]
    if M!=0: return round(N/M, 2)

mc = []
mc_jit = []

start = datetime.now()
for i in range(7): mc.append(monte_carlo(10**i))
end = datetime.now()

print("Usual:", mc, "in", end-start, "sec")

start_jit = datetime.now()
for i in range(7): mc_jit.append(monte_carlo_jit(10**i))
end_jit = datetime.now()

print("JIT:", mc_jit, "in",end_jit - start_jit, "sec")
print("JIT is", round((end - start)/(end_jit - start_jit), 3), "times faster.")

