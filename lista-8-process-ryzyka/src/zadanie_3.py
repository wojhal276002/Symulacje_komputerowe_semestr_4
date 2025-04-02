import matplotlib.pyplot as plt
import numpy as np
import scipy.special


def ruina_paryska(funk, rozklad, param):
    lamb = 1
    r_0 = 10
    funkc = funk
    p = param
    te = [0]
    iy = [0]
    I = 0
    T = 10
    T_i = 0
    zegar = 4
    while T_i <= T:
        t = np.random.exponential(1 / lamb)
        T_i += t
        I += 1
        iy.append(I)
        if T_i > T:
            te.append(T)
            break
        te.append(T_i)
    Rt = np.zeros(I + 1)
    zetas = rozklad(p, size=1000)
    k = 0
    bankructwo = 0
    while k <= I:
        wart = r_0 + funkc * te[k] - sum(zetas[:k])
        print(wart)
        Rt[k] = wart
        if wart <= 0:
            bankructwo += 1
        if k > 0 and Rt[k - 1] <= 0 and Rt[k] > 0:
            bankructwo = 0
        if bankructwo == zegar:
            break
        k += 1
    plt.plot(iy, np.zeros(I + 1))
    iy_1, Rt_1 = iy[: k + 1], Rt[: k + 1]
    plt.plot(iy_1, Rt_1)
    plt.xlim(0, I)
    if min(Rt_1) >= 5:
        plt.ylim(-1, max(Rt_1) + 5)
    else:
        plt.ylim(min(Rt) - 5, max(Rt_1) + 5)
    plt.show()


ruina_paryska(2, np.random.pareto, 1)
