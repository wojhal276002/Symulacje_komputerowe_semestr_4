import numpy as np
import matplotlib.pyplot as plt
import random
import time


M = 2**89 - 1
k = 9
Lag = 10**3
N = 10**4
def ACORN(N, k, M, Lag):
    lista = [np.zeros(N+Lag+1) for _ in range(k+1)]
    seed  = random.randint(1,M-1)
    for i in range(len(lista[0])):
        lista[0][i] = seed
    pozycja = 1
    rzad = 1
    start = time.time()
    while True:
        lista[rzad][pozycja] = (lista[rzad][pozycja-1]+lista[rzad-1][pozycja])%M
        pozycja+=1
        if pozycja==N+Lag+1:
            if rzad == k:
                Yk = lista[k][Lag::]/M
                break
            rzad += 1
            pozycja = 1
    return Yk

Yk = ACORN(N, k, M, Lag)
xs = range(0,N+1)
print(len(Yk))
plt.scatter(xs,Yk,s=3)
plt.show()
plt.scatter(Yk[:-1],Yk[1:],s=3)
plt.show()
plt.hist(Yk,bins=20)
plt.show()
start1 = time.time()
Y_proba = np.random.uniform(0,1,9000)
end1 = time.time()
czas1 = end1-start1


