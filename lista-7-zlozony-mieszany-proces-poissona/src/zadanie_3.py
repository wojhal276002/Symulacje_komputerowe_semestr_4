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
        while T_i_exp <= T:
            U_exp = np.random.uniform(0, 1)
            T_i_exp -= (1 / L_exp) * np.log(U_exp)
            iy_exp.append(I_exp)
            I_exp += 1
            if T_i_exp > T:
                te_exp.append(T)
            else:
                te_exp.append(T_i_exp)
                iy_exp.append(I_exp)
                te_exp.append(T_i_exp)
        plt.plot(te_exp, iy_exp, "blue", label="exp(1)")
        I = 0
        L = np.random.uniform(0, 10)
        T_i = 0
        while T_i <= T:
            U = np.random.uniform(0, 1)
            T_i -= (1 / L) * np.log(U)
            iy.append(I)
            I += 1
            if T_i > T:
                te.append(T)
            else:
                te.append(T_i)
                iy.append(I)
                te.append(T_i)
        plt.plot(te, iy, "orange", label="u(0,10)")
    else:
        te = [0]
        iy = [0]
        te_exp = [0]
        iy_exp = [0]
        I_exp = 0
        L_exp = np.random.exponential(1)
        T_i_exp = 0
        while T_i_exp <= T:
            U_exp = np.random.uniform(0, 1)
            T_i_exp -= (1 / L_exp) * np.log(U_exp)
            iy_exp.append(I_exp)
            I_exp += 1
            if T_i_exp > T:
                te_exp.append(T)
            else:
                te_exp.append(T_i_exp)
                iy_exp.append(I_exp)
                te_exp.append(T_i_exp)
        plt.plot(te_exp, iy_exp, "blue")
        I = 0
        L = np.random.uniform(0, 10)
        T_i = 0
        while T_i <= T:
            U = np.random.uniform(0, 1)
            T_i -= (1 / L) * np.log(U)
            iy.append(I)
            I += 1
            if T_i > T:
                te.append(T)
            else:
                te.append(T_i)
                iy.append(I)
                te.append(T_i)
        plt.plot(te, iy, "orange")
print(te_exp, iy_exp)
plt.legend()
plt.title("Mieszany rozkład Poisson (1)")
plt.show()
