import random
office = [[], [], []]
Name = ["A", "B", "C", "D", "E", "F", "G"]
for i in range(len(Name)):
    x = random.randint(0, 2)
    office[x].append(Name[i])
print(office)
