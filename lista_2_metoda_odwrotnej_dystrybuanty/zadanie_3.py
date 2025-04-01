import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def table_lookup(prawdop):
    suma = 0
    table = []
    for prawd in prawdop:
        suma += prawd
        table.append(suma)
    return table


def probka_pojedyncza(table):
    x = np.random.rand()
    for i in range(len(table)):
        if x <= table[i]:
            return i+1


prawdopodobienstwa = [0.1, 0.2, 0.1, 0.1, 0.3, 0.1,0.1]

test = [probka_pojedyncza(table_lookup(prawdopodobienstwa)) for j in range(100000)]
new_test = []
for i in range(1,11,1):
    nowa = 0
    for x in test:
        if x == i:
            nowa += 1
    new_test.append(nowa/100000)
print(new_test)
        


plt.title("Dystrybuanta listy prawdopodobieństwo")
sns.ecdfplot(test)
plt.show()

plt.title("Rozkład wartości przyporządkowanych do listy prawdopodobieństwo")
plt.bar(range(1,11,1),new_test,width=0.5)
plt.ylim(0,0.5)
plt.show()
