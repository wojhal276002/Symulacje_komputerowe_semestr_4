import matplotlib.pyplot as plt
import numpy as np


def gestosc_1(alfa, n):
    akceptacja = np.zeros(n)
    c_alfa = alfa + 1
    lacznie = 0
    index = 0
    while akceptacja[n - 1] == 0:
        lacznie += 1
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, c_alfa)
        if u2 <= (alfa + 1) * u1**alfa:
            akceptacja[index] = u1
            index += 1
    efektywnosc = n / lacznie
    return (akceptacja, efektywnosc)


n = 100
alfy = 150
result = np.zeros(alfy)
for i in range(alfy):
    result[i] = gestosc_1(i, n)[1]


xs = np.linspace(1, alfy, alfy)
plt.plot(xs, result)
plt.xlabel("Wartości alfy")
plt.ylabel("Część prób, które były zaakceptowane (trafione)")
plt.title("Efektywność")
plt.show()
