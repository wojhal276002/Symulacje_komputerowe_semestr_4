import sys
import time
import tracemalloc

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import poisson

# rozklad geometryczny
n_geom = 1000
p = 1
xs_geom = np.linspace(0, 10, 1000)


def odwr_dyst_geom(num, p):
    sample = np.random.uniform(0, 1, num)
    return np.ceil((np.log(sample) / np.log(1 - p)))


def dist_geom(x, p):
    return 1 - (1 - p) ** x


probka_geom = odwr_dyst_geom(n_geom, 1 / 2)
probka_statystyczna_geom = np.random.geometric(1 / 2, n_geom)

plt.title("Porównanie dystrybuant rozkładu Geom")
plt.plot(
    xs_geom, dist_geom(xs_geom, 1 / 2), label="dystrybuanta teoretyczna rozkładu Geom"
)
sns.ecdfplot(probka_geom, label="dystrybuanta empiryczna Geom")
sns.ecdfplot(probka_statystyczna_geom, label="dystrybuanta Geom z numpy")
plt.legend()
plt.show()

# czas i pamiec
xs_geom_1 = np.linspace(10**5, 10**6, 10)
sys.setrecursionlimit(12000)


def odwr_dyst_geom_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            odwr_dyst_geom(i, 1 / 2)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        odwr_dyst_geom(start, 1 / 2)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


def odwr_numpy_geom_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            np.random.geometric(1 / 2, i)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        np.random.normal(1 / 2, start)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


czas_geom_1, pamiec_geom_1 = odwr_dyst_geom_czas_pamiec()
czas_geom_2, pamiec_geom_2 = odwr_numpy_geom_czas_pamiec()
plt.plot(xs_geom_1, czas_geom_1, "bD", label="czas-odwr")
plt.plot(xs_geom_1, czas_geom_2, "rD", label="czas-numpy")
plt.legend()
plt.show()

plt.plot(xs_geom_1, pamiec_geom_1, "rD", label="peak-odw_dyst")
plt.plot(xs_geom_1, pamiec_geom_2, "gD", label="peak-np")
plt.title("Zależność między długością próbki a zużyciem pamięci")
plt.xlabel("Długość próbki")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()

# rozklad poissona

n_pois = 1000
lambd = 2
xs_pois = np.linspace(0, 10, 1000)


def odwr_dyst_pois(num, p):
    sample = np.random.uniform(0, 1, num)
    result = []
    for u in sample:
        j = 0
        p = np.exp(-lambd)
        F = p
        while u > F:
            p *= lambd / (j + 1)
            F += p
            j += 1
        result.append(j)
    return result


probka_pois = odwr_dyst_pois(n_pois, lambd)
probka_statystyczna_pois = np.random.poisson(lambd, n_pois)

plt.title("Porównanie dystrybuant rozkładu Poisson")
plt.plot(
    xs_pois,
    poisson.cdf(xs_pois, lambd),
    label="dystrybuanta teoretyczna rozkładu Poisson",
)
sns.ecdfplot(probka_pois, label="dystrybuanta empiryczna Poisson")
sns.ecdfplot(probka_statystyczna_pois, label="dystrybuanta Poisson z numpy")
plt.legend()
plt.show()

# czas i pamiec
xs_pois_1 = np.linspace(10**4, 10**5, 10)


def odwr_dyst_pois_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**5, 10**4):
        czas = 0
        for n in range(10):
            start = time.time()
            odwr_dyst_pois(i, lambd)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**4
    stop = 10**5
    for i in range(10):
        tracemalloc.start()
        odwr_dyst_pois(start, lambd)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


def odwr_numpy_pois_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**5, 10**4):
        czas = 0
        for n in range(10):
            start = time.time()
            np.random.poisson(lambd, i)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**4
    stop = 10**5
    for i in range(10):
        tracemalloc.start()
        np.random.poisson(lambd, start)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


czas_pois_1, pamiec_pois_1 = odwr_dyst_pois_czas_pamiec()
czas_pois_2, pamiec_pois_2 = odwr_numpy_pois_czas_pamiec()
plt.plot(xs_pois_1, czas_pois_1, "bD", label="czas-odwr")
plt.plot(xs_pois_1, czas_pois_2, "rD", label="czas-numpy")
plt.legend()
plt.show()

plt.plot(xs_pois_1, pamiec_pois_1, "rD", label="peak-odw_dyst")
plt.plot(xs_pois_1, pamiec_pois_2, "gD", label="peak-np")
plt.title("Zależność między długością próbki a zużyciem pamięci")
plt.xlabel("Długość próbki")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()
