import random
import matplotlib.pyplot as plt
jas_bankrut = []
grzes_bankrut = []
for c in range(0,51):
    W_G = 0
    W_J = 0
    for i in range(1000):
        G_B = 20
        J_B = c
        while True:
            list = []
            while True:
                x = random.uniform(0,1)
                if x>0.5:
                    list.append("O")
                else:
                    list.append("R")
                if len(list) != 3:
                    continue
                else:
                    if list == ["O", "O", "R"]:
                        G_B -= 1
                        J_B += 1
                        break
                    elif list == ["O", "R", "R"]:
                        J_B -= 1
                        G_B += 1
                        break
                    else:
                        list = list[1:]
            if G_B == 0:
                W_J += 1
                break
            elif J_B == 0:
                W_G += 1
                break
            else:
                continue
    jas = W_G/1000
    grzes = W_J/1000
    jas_bankrut.append(jas)
    grzes_bankrut.append(grzes)

x_var = range(0,51)
plt.plot(x_var,jas_bankrut,color="b", label="jas")
plt.plot(x_var,grzes_bankrut, color="r", label="grzes")
plt.legend()
plt.show()
