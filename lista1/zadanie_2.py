import random
import matplotlib.pyplot as plt

def corput(n, base):
    if n == 0:
        return 0
    else:
        konwersja = ""
        while n > 0:
            krok = n % base
            n //= base
            konwersja += str(krok)
    odwrocone = "0."+konwersja
    lista_elem = [int(odwrocone[i]) for i in range(2,len(odwrocone))]
    lista_wartosci = [lista_elem[x]*base**(-(x+1)) for x in range(len(lista_elem))]
    return sum(lista_wartosci)

def corput_sekwencja(n, b):
    sekwencja = []
    for i in range(n):
        sekwencja.append(corput(i,b))
    return sekwencja

ys1 = corput_sekwencja(1000,2)
ys2 = [random.uniform(0,1) for j in range(1000)]
xs = range(1,1001)
print(len(ys1))
plt.scatter(xs,ys1)
plt.scatter(xs,ys2)
plt.title("Liczby kwazilosowe z ciągu van der Corputa")
plt.show()


