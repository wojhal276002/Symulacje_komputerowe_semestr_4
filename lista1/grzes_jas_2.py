import random
W_G = 0
W_J = 0
for i in range(1000):
    G_B = 25
    J_B = 5
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

print(W_J/1000)

    