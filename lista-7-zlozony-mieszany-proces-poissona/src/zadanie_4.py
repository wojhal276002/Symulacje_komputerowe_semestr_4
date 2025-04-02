import random

import matplotlib.pyplot as plt
import numpy as np

trajektorie = 10
T = 10
for i in range(trajektorie):
    if i == 0:
        te = [0]
        iy = [0]
        te_exp = [0]
        iy_exp = [0]
        I_exp = 0
        L_exp = np.random.exponential(1)
        T_i_exp = 0
        n_exp = np.random.poisson(L_exp * T)
        skok_exp = sorted([np.random.uniform(0, T) for i in range(n_exp)] * 2)
        for c in range(len(skok_exp)):
            if c % 2 == 0:
                iy_exp.append(I_exp)
            else:
                I_exp += 1
                iy_exp.append(I_exp)
            te_exp.append(skok_exp[c])
        plt.plot(te_exp, iy_exp, "blue", label="exp(1)")
        I = 0
        L = np.random.uniform(0, 10)
        T_i = 0
        n = np.random.poisson(T * L)
        skok = sorted([np.random.uniform(0, T) for i in range(n)] * 2)
        for c in range(len(skok)):
            if c % 2 == 0:
                iy.append(I)
            else:
                I += 1
                iy.append(I)
            te.append(skok[c])
        plt.plot(te, iy, "orange", label="u(0,10)")
    else:
        te = [0]
        iy = [0]
        te_exp = [0]
        iy_exp = [0]
        I_exp = 0
        L_exp = np.random.exponential(1)
        T_i_exp = 0
        n_exp = np.random.poisson(T * L_exp)
        skok_exp = sorted([np.random.uniform(0, T) for i in range(n_exp)] * 2)
        for c in range(len(skok_exp)):
            if c % 2 == 0:
                iy_exp.append(I_exp)
            else:
                I_exp += 1
                iy_exp.append(I_exp)
            te_exp.append(skok_exp[c])
        plt.plot(te_exp, iy_exp, "blue")
        I = 0
        L = np.random.uniform(0, 10)
        T_i = 0
        n = np.random.poisson(T * L)
        skok = sorted([np.random.uniform(0, T) for i in range(n)] * 2)
        for c in range(len(skok)):
            if c % 2 == 0:
                iy.append(I)
            else:
                I += 1
                iy.append(I)
            te.append(skok[c])
        plt.plot(te, iy, "orange")
plt.legend()
plt.title("Mieszany rozkład Poisson (2)")
plt.show()
