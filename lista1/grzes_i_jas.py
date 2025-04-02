import random
G = 0
J = 0
for n in range(1000):
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
                J+=1
                break
            elif list == ["O", "R", "R"]:
                G+=1
                break
            else:
                list = list[1:]
print(G/1000)

