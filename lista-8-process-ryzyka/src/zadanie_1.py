import matplotlib.pyplot as plt
import numpy as np
import scipy.special


def proces_ryzyka(funk, rozklad, param):
    lamb = 1
    r_0 = 10
    funkc = funk
    p = param
    te = [0]
    iy = [0]
    I = 0
    T = 10
    T_i = 0
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
    while k <= I:
        wart = r_0 + funkc * te[k] - sum(zetas[:k])
        print(wart)
        Rt[k] = wart
        if wart <= 0:
            break
        k += 1
    iy, Rt = iy[: k + 1], Rt[: k + 1]
    plt.plot(iy, Rt)
    plt.xlim(0, I)
    plt.show()


proces_ryzyka(2, np.random.weibull, 1)
