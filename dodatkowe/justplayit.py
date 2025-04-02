import matplotlib.pyplot as plt
import numpy as np
import scipy.special

# 2 numer indeksu 276002


def ruina_paryska(A: int):
    """
    Funkcja zwracająca informację czy ruina wystąpiła w ciągu 5 lat dla podanego parametru A

    Parametry:
    A (int): parametr okre

    Zwraca:
    informacja zwrotna o ruinie

    """
    c = A / 3
    r_0 = 2 * A
    T = 2*np.pi
    xs = np.linspace(0, T, 1000)
    lamb = lambda t: 1 + np.sin(t)
    lambd_max = max(lamb(xs))
    te = [0]
    iy = [0]
    I = 0
    t = 0
    zegar = 5
    nowe_T = 365*5
    while t <= nowe_T:
        U = np.random.uniform(0, 1)
        t = t - 1 / lambd_max * np.log(U)
        if t > nowe_T:
            te.append(nowe_T)
            break
        else:
            U_1 = np.random.uniform(0, 1)
            if U_1 <= lamb(t) / lambd_max:
                iy.append(I)
                I += 1
                te.append(t)
        te.append(t)
        plt.plot()
    Rt = np.zeros(I + 1)
    zetas = np.random.exponential(c, size=I)
    k = 0
    bankructwo = 0
    koniec = 0
    while k <= I:
        wart = r_0 + c * te[k] - sum(zetas[:k])
        Rt[k] = wart
        if wart <= 0:
            if wart < -10:
                Rt[k:] = wart
                koniec += 1
                break
            bankructwo += 1
        if k > 0 and Rt[k - 1] <= 0 and Rt[k] > 0:
            bankructwo = 0
        if bankructwo == zegar:
            Rt[k:] = wart
            koniec += 1
            break
        k += 1
    plt.step(iy,Rt)
    if koniec == 1:
        return koniec, iy[k+1]
    else:
        return Rt[k-1], iy[k-1]

N = 50
C = np.zeros(N)
p = 0
ruiny = np.zeros(365*5)
while p < N:
    ruina, dzien = ruina_paryska(9)
    if ruina == 1:
        C[p] = ruina
        ruiny[dzien] += 1
    p += 1
print(
    f"Prawdopodobieństwo ruiny w ciągu 5 lat dla podanych parametrów wynosi: {sum(C)/N}"
)
plt.show()