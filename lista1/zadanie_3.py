import random 
import math
n=14000
lezy = 0
n_lezy = 0
for i in range(n):
    cartesian = (random.uniform(0,1), random.uniform(0,1))
    if math.sqrt(cartesian[0]**2+cartesian[1]**2) <= 1:
        lezy+=1
    else:
        n_lezy+=1

pi = (4*lezy)/(lezy+n_lezy)
print("uniform:",pi)
#"------------"

def generator_lcg(n,seed):
    lezy = 0
    n_lezy = 0
    a = 16807
    m = 2**32 - 1
    c = 0
    liczby = []
    for i in range(n):
        seed_1 = (a*seed + c) % m
        seed_2 = (a*seed_1 + c) % m
        cartesian = (seed_2/m,seed_1/m)
        if math.sqrt(cartesian[0]**2+cartesian[1]**2) <= 1:
            lezy+=1
        else:
            n_lezy+=1
        seed = seed_2
    return (4*lezy)/(lezy+n_lezy)

print("lcg:",generator_lcg(n,10))
#"------------"

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

def halton(n, b, k):
    lezy = 0
    n_lezy = 0
    if math.gcd(b,k) == 1:
        cartesian = (corput_sekwencja(n,b), corput_sekwencja(n,k))
        for i in range(len(cartesian[0])):
            if math.sqrt(cartesian[0][i]**2+cartesian[1][i]**2) <= 1:
                lezy+=1
            else:
                n_lezy+=1
        return (4*lezy)/(lezy+n_lezy)
    else:
        raise ValueError("WZGLĘDNOŚĆ PIERWSZA BAZ NIE SPEŁNONA")

print("halton:",halton(14000,2,3))