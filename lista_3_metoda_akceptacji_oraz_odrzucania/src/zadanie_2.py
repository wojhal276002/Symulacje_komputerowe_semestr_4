import matplotlib.pyplot as plt
import numpy as np


def gestosc_sin(n):
    c_alfa = np.pi / 2
    akceptacja = np.zeros(n)
    lacznie = 0
    index = 0
    while akceptacja[n - 1] == 0:
        lacznie += 1
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, np.pi / 2)
        if u1 <= np.sin(u2):
            akceptacja[index] = u2
            index += 1
    efektywnosc = n / lacznie
    return (akceptacja, efektywnosc)


alfy = 1000
result = np.zeros(alfy)
for i in range(1, alfy + 1):
    result[i - 1] = gestosc_sin(i)[1]

xs = np.linspace(1, alfy, alfy)
plt.plot(xs, result)
plt.xlabel("Liczba potrzebnych trafień")
plt.ylabel("Część prób, które były zaakceptowane (trafione)")
plt.title("Efektywność symulacji X")
plt.show()


def gestosc_sin2(n):
    c_alfa = (np.pi * np.pi**2) / 8
    akceptacja = np.zeros(n)
    lacznie = 0
    index = 0
    while akceptacja[n - 1] == 0:
        lacznie += 1
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, np.pi**2 / 4)
        if u1 <= np.sin(np.sqrt(u2)):
            akceptacja[index] = np.sqrt(u2)
            index += 1
        efektywnosc = n / lacznie
    return (akceptacja, efektywnosc)


alfy_2 = 1000
result_2 = np.zeros(alfy_2)
for j in range(1, alfy_2 + 1):
    result_2[j - 1] = gestosc_sin2(j)[1]

xs2 = np.linspace(1, alfy_2, alfy_2)
plt.plot(xs, result, label="X")
plt.plot(xs2, result_2, label="Y=X^2")
plt.ylabel("Część prób, które były zaakceptowane (trafione)")
plt.xlabel("Liczba potrzebnych trafień")
plt.title("Porównanie efektywności obu symulacji")
plt.legend()
plt.show()
