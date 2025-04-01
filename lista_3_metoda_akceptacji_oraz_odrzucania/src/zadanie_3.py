import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm


def exp(num):
    sample = np.random.rand(num)
    return -1 * np.log(sample)


def normal_przez_exp(n, sigma, mi):
    akceptacja = np.zeros(n)
    lacznie = 0
    index = 0
    while akceptacja[n - 1] == 0:
        lacznie += 1
        u1 = np.random.uniform(0, 1)
        u2 = exp(1)
        if u1 <= np.exp(-((u2 - 1) ** 2) / 2):
            u3 = np.random.uniform(0, 1)
            if u3 <= 0.5:
                akceptacja[index] = u2 / mi + sigma
            else:
                akceptacja[index] = -u2 / mi + sigma
            index += 1
    return akceptacja


sample = normal_przez_exp(10000, 0, 1)

xs = np.linspace(-5, 5, 10000)
sns.kdeplot(sample, label="gęstość przez wykładniczy")
plt.plot(xs, norm.pdf(xs, 0,1), label="gęstość teoretyczna")
plt.title("Porównanie gęstości")
plt.ylim(0, 0.5)
plt.legend()
plt.show()
