import random
import matplotlib.pyplot as plt


def corput_konwersja(n, base):
    q = 0
    bk = 1 / base

    while n > 0:
        q += (n % base) * bk
        n //= base
        bk /= base

    return q

print(corput_konwersja(13,10))

def van_der_corput_sequence(n, b):
    result = []
    for i in range(n):
        result.append(corput_konwersja(i,b))
    return result

ys1 = van_der_corput_sequence(1000,2)
ys2 = [random.uniform(0,1) for _ in range(1000)]
xs = range(1,1001)
plt.scatter(xs,ys1)
plt.scatter(xs,ys2)
plt.title("Liczby kwazilosowe z ciągu van der Corputa")
plt.show()