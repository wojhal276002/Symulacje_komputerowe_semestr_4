import matplotlib.pyplot as plt
import random

n = 1000

def generator_lcg(n,seed):
    a = 16807
    m = 2**32 - 1
    c = 0
    liczby = []
    for i in range(n):
        liczby.append(seed/m)
        seed_1 = (a*seed + c) % m
        seed = seed_1
    return liczby 
    
ys1 = generator_lcg(n,10)
ys2 = [random.uniform(0,1) for _ in range(1000)]
xs = range(1,1001)

plt.scatter(xs,ys1,label="lcg")
plt.scatter(xs,ys2,label="uniform", color="r")
plt.legend()
plt.show()
