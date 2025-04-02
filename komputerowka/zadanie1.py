import matplotlib.pyplot as plt
import numpy as np
import pylab as py
import seaborn as sns
from scipy import stats

# 276002 więc 2%2
m = 0
s = 1
N = 2000
m_indeks = 2 % 2


def tuzin(N: int, m: float = 0, s: float = 1) -> list:
    """
    Funkcja zwracająca Y- N liczb z rozkładu normalnego generowanego metodą tuzina

    Parametry:
    N (int): liczba liczb z rozkładu normalnego do wygenerowania
    m(float): wartość oczekiwana rozkładu normalnego (domyślnie 0)
    s (float): parametr sigma^2 (domyślnie 1)

    Zwraca:
    Y (list): lista N liczb z rozkładu normalnego wygenerowanego metodą tuzina

    """
    S = sum(np.random.rand(12, N))
    X = S - 6

    Y = s * X + m
    return Y


# granice rozkładu normalnego generowanego
ts = np.linspace(-4, 4, 1000)
tuzin_proba = tuzin(N)
print(tuzin_proba)

plt.hist(tuzin_proba, bins=20, density=True, label="Histogram próbki")
plt.plot(ts, stats.norm.pdf(ts, m_indeks, s), label="Gęstość teoretyczna")
plt.legend()
plt.title("Histogram vs gęstość teoretyczna")
plt.grid()
plt.show()

sns.ecdfplot(tuzin_proba, label="Dyst empir")
plt.plot(ts, stats.norm.cdf(ts, m_indeks, s), label="Dyst teor")
plt.legend()
plt.title("Dystrybunata empiryczna vs dystrybuanta teoretyczna")
plt.grid()
plt.show()


measurements = np.random.normal(m_indeks, s, size=N)
stats.probplot(tuzin_proba, dist="norm", plot=py)
py.show()
