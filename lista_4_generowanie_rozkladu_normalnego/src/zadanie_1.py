import time

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm


def polar_box_muller(n, mi, sigma):
    akceptacja = np.zeros(n)
    iter = 0
    while akceptacja[n - 1] == 0:
        u1 = np.random.uniform(-1, 1)
        u2 = np.random.uniform(-1, 1)
        v1, v2 = 2 * u1 - 1, 2 * u2 - 1
        w = v1**2 + v2**2
        if w < 1:
            y = np.sqrt(-2 * np.log(w) / w)
            x1, x2 = v1 * y, v2 * y
            akceptacja[iter] = sigma * x1 + mi
            if iter + 1 != n:
                akceptacja[iter + 1] = sigma * x2 + mi
            iter += 2
    return akceptacja


akceptacja_box_muller = polar_box_muller(10001, 0, 1)
xs = np.linspace(-5, 5, 100)
sns.kdeplot(akceptacja_box_muller, label="gest empir")
plt.plot(xs, norm.pdf(xs, 0, 1), label="gest teor")
plt.title("Metoda Boxa-Mullera")
plt.legend()
plt.show()


def polar_marsaglia(n, mi, sigma):
    akceptacja = np.zeros(n)
    iter = 0
    while akceptacja[n - 1] == 0:
        y1 = np.random.uniform(-1, 1)
        y2 = np.random.uniform(-1, 1)
        r = y1**2 + y2**2
        if r < 1:
            y = np.sqrt(-2 * np.log(r) / r)
            x1, x2 = y1 * y, y2 * y
            akceptacja[iter] = x1 * sigma + mi
            if iter + 1 != n:
                akceptacja[iter + 1] = x2 * sigma + mi
            iter += 2
    return akceptacja


akceptacja_mars = polar_marsaglia(10001, 0, 1)
xs = np.linspace(-5, 5, 100)
sns.kdeplot(akceptacja_mars, label="gest empir")
plt.plot(xs, norm.pdf(xs, 0, 1), label="gest teor")
plt.title("Metoda Marsagli")
plt.legend()
plt.show()

lista_czasow_1 = np.zeros(10)
lista_czasow_2 = np.zeros(10)
xs = np.linspace(1000, 10000, 10)
ind = 0
for i in xs:
    czas_1 = 0
    czas_2 = 0
    for n in range(50):
        print(i)
        start_1 = time.time()
        polar_box_muller(int(i), 0, 1)
        end_1 = time.time()
        czas_1 += end_1 - start_1
        start_2 = time.time()
        polar_marsaglia(int(i), 0, 1)
        end_2 = time.time()
        czas_2 += end_2 - start_2
    lista_czasow_1[ind] = czas_1
    lista_czasow_2[ind] = czas_2
    ind += 1


plt.plot(xs, lista_czasow_1, label="czas box_muller")
plt.plot(xs, lista_czasow_2, label="czas marsaglia")
plt.legend()
plt.show()
