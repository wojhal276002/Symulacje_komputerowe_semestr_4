import sys
import time
import tracemalloc

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import cauchy, norm

# rozklad wykladniczy
n_exp = 1000
lambd = 2
lambd_np = 1 / lambd
xs_exp = np.linspace(0, 5, 1000)


def odwr_dyst_exponential(num, lambd):
    sample = np.random.uniform(0, 1, num)
    return (-1 * np.log(1 - sample)) / lambd


def gest_exponential(x, lambd):
    return lambd * np.exp((-1) * lambd * x)


def dist_exponential(x, lambd):
    return 1 - np.exp((-1) * lambd * x)


probka_exp = odwr_dyst_exponential(n_exp, lambd)
probka_statystyczna_exp = np.random.exponential(lambd_np, 1000)

plt.title("Porównanie dystrybuant rozkładu Exp")
plt.plot(xs_exp, dist_exponential(xs_exp, lambd), label="dystrybuanta teoretyczna Exp")
sns.ecdfplot(probka_exp, label="dystrybuanta empiryczna Exp")
sns.ecdfplot(probka_statystyczna_exp, label="dystrybuanta Exp z modułu numpy")
plt.legend()
plt.show()

plt.title("Porównanie gestosci rozkładu Exp")
plt.plot(xs_exp, gest_exponential(xs_exp, lambd), label="gestosc teoretyczna Exp")
sns.kdeplot(probka_exp, label="gestosc empiryczna Exp")
sns.kdeplot(probka_statystyczna_exp, label="gestosc Exp z modułu numpy")
plt.legend()
plt.show()

# czas i pamiec
xs_exp_1 = np.linspace(10**6, 10**7, 10)
sys.setrecursionlimit(12000)


def odwr_dyst_exp_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**7, 10**6):
        czas = 0
        for n in range(10):
            start = time.time()
            odwr_dyst_exponential(i, lambd)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**6
    stop = 10**7
    for i in range(10):
        tracemalloc.start()
        odwr_dyst_exponential(start, lambd)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


def odwr_numpy_exp_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**7, 10**6):
        czas = 0
        for n in range(10):
            start = time.time()
            np.random.exponential(lambd_np, i)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**6
    stop = 10**7
    for i in range(10):
        tracemalloc.start()
        np.random.exponential(lambd_np, start)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


czas_exp_1, pamiec_exp_1 = odwr_dyst_exp_czas_pamiec()
czas_exp_2, pamiec_exp_2 = odwr_numpy_exp_czas_pamiec()
plt.plot(xs_exp_1, czas_exp_1, "bD", label="czas-odwr")
plt.plot(xs_exp_1, czas_exp_2, "rD", label="czas-numpy")
plt.legend()
plt.show()

plt.plot(xs_exp_1, pamiec_exp_1, "rD", label="peak-odw_dyst")
plt.plot(xs_exp_1, pamiec_exp_2, "gD", label="peak-np")
plt.title("Zależność między długością próbki a zużyciem pamięci")
plt.xlabel("Długość próbki")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()

# rozklad normalny
n_norm = 1000
mi = 0
sigma = 1
xs_norm = np.linspace(-10, 10, 1000)


def odwr_dyst_normal(num, mi, sigma):
    sample = np.random.uniform(0, 1, num)
    return norm.ppf(sample, loc=mi, scale=sigma ** (0.5))


probka_norm = odwr_dyst_normal(n_norm, mi, sigma)
probka_statystyczna_norm = np.random.normal(0, 1, 1000)

plt.title("Porównanie dystrybuant rozkładu Normal")
plt.plot(
    xs_norm,
    norm.cdf(xs_norm, loc=mi, scale=sigma),
    label="dystrybuanta teoretyczna Normal",
)
sns.ecdfplot(probka_norm, label="dystrybuanta empiryczna Normal")
sns.ecdfplot(probka_statystyczna_norm, label="dystrybuanta Normal z numpy")
plt.legend()
plt.show()

plt.title("Porównanie gestosci rozkładu Normal")
plt.xlim(-40, 10)
plt.plot(
    xs_norm, norm.pdf(xs_norm, loc=mi, scale=sigma), label="gestosc teoretyczna Normal"
)
sns.kdeplot(probka_norm, label="gestosc empiryczna Normal")
sns.kdeplot(probka_statystyczna_norm, label="gestosc Normal z numpy")
plt.legend()
plt.show()

# czas i pamiec
xs_norm_1 = np.linspace(10**5, 10**6, 10)
sys.setrecursionlimit(12000)


def odwr_dyst_exp_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            odwr_dyst_normal(i, mi, sigma)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        odwr_dyst_normal(start, mi, sigma)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


def odwr_numpy_exp_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            np.random.normal(0, 1, i)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        np.random.normal(0, 1, start)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


czas_exp_1, pamiec_exp_1 = odwr_dyst_exp_czas_pamiec()
czas_exp_2, pamiec_exp_2 = odwr_numpy_exp_czas_pamiec()
plt.plot(xs_norm_1, czas_exp_1, "bD", label="czas-odwr")
plt.plot(xs_norm_1, czas_exp_2, "rD", label="czas-numpy")
plt.legend()
plt.show()

plt.plot(xs_norm_1, pamiec_exp_1, "rD", label="peak-odw_dyst")
plt.plot(xs_norm_1, pamiec_exp_2, "gD", label="peak-np")
plt.title("Zależność między długością próbki a zużyciem pamięci")
plt.xlabel("Długość próbki")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()


# rozklad cauchy
n_cau = 1000
gamma = 1
mu = -2
xs_cau = np.linspace(-10, 10, 1000)


def odwr_dyst_cauchy(num, gamma, mu):
    sample = np.random.uniform(0, 1, num)
    return gamma * np.tan(np.pi * (sample - 1 / 2)) + mu


def gest_cauchy(x, gamma, mu):
    return gamma / (np.pi * gamma**2 + np.pi * (x - mu) ** 2)


def dist_cauchy(x, gamma, mu):
    return 1 / np.pi * np.arctan((x - mu) / gamma) + 1 / 2


probka_cau = odwr_dyst_cauchy(n_cau, gamma, mu)
probka_statystyczna_cau = cauchy.rvs(loc=-2, size=n_cau)

plt.title("Porównanie dystrybuant rozkładu Cauchy")
plt.xlim(-10, 10)
plt.plot(
    xs_cau, dist_cauchy(xs_cau, gamma, mu), label="dystrybuanta teoretyczna Cauchy"
)
sns.ecdfplot(probka_cau, label="dystrybuanta empiryczna Cauchy")
sns.ecdfplot(probka_statystyczna_cau, label="dystrybuanta Cauchy z modułu scipy")
plt.legend()
plt.show()

plt.title("Porównanie gestosci rozkładu Cauchy")
plt.plot(xs_cau, gest_cauchy(xs_cau, gamma, mu), label="gestosc teoretyczna Cauchy")
sns.kdeplot(probka_cau, label="gestosc empiryczna Cauchy")
sns.kdeplot(probka_statystyczna_cau, label="gestosc Cauchy z modułu scipy")
plt.legend()
plt.show()

# czas i pamiec
xs_cau_1 = np.linspace(10**5, 10**6, 10)


def odwr_dyst_cau_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            odwr_dyst_cauchy(i, gamma, mu)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        odwr_dyst_cauchy(start, gamma, mu)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


def odwr_numpy_cau_czas_pamiec():
    lista_czasow = []
    for i in range(0, 10**6, 10**5):
        czas = 0
        for n in range(10):
            start = time.time()
            cauchy.rvs(loc=-2, size=n_cau)
            end = time.time()
            czas += end - start
        lista_czasow.append(czas / 10)
    pamiec_top = []
    start = 10**5
    stop = 10**6
    for i in range(10):
        tracemalloc.start()
        cauchy.rvs(loc=-2, size=n_cau)
        top = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        pamiec_top.append(top)
        start += stop // 10
    return lista_czasow, pamiec_top


czas_cau_1, pamiec_cau_1 = odwr_dyst_cau_czas_pamiec()
czas_cau_2, pamiec_cau_2 = odwr_numpy_cau_czas_pamiec()

plt.plot(xs_cau_1, czas_cau_1, "bD", label="czas-odwr")
plt.plot(xs_cau_1, czas_cau_2, "rD", label="czas-scipy")
plt.legend()
plt.show()

plt.plot(xs_cau_1, pamiec_cau_1, "rD", label="peak-odw_dyst")
plt.plot(xs_cau_1, pamiec_cau_2, "gD", label="peak-scipy")
plt.title("Zależność między długością próbki a zużyciem pamięci")
plt.xlabel("Długość próbki")
plt.ylabel("Zużycie pamięci")
plt.legend()
plt.show()
