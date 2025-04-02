import matplotlib.pyplot as plt
import numpy as np

lamb = 1
T = 10
S_all1 = []
Nt_all1 = []
powt = 5
for i in range(powt):
    t = 0
    S = []
    Nt = []
    while t <= T:
        U = np.random.uniform(0, 1)
        t = t - (np.log(U) / lamb)
        S.append(t)
        Nt.append(np.random.normal(0, 1))
    S_all1.append(S)
    Nt_all1.append(Nt)
for i in range(powt):
    plt.step(S_all1[i], np.cumsum(Nt_all1[i]))
plt.title("Złożony proces Poissona N(0,1)")
plt.show()

S_all2 = []
Nt_all2 = []
for i in range(powt):
    t = 0
    S = []
    Nt = []
    while t <= T:
        U = np.random.uniform(0, 1)
        t = t - (np.log(U) / lamb)
        S.append(t)
        Nt.append(np.random.standard_cauchy())
    S_all2.append(S)
    Nt_all2.append(Nt)
for i in range(powt):
    plt.step(S_all2[i], np.cumsum(Nt_all2[i]))
plt.title("Złożony proces Poissona C(0,1)")
plt.show()
