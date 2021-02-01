import random
for i in range(1,10,1):
    for j in range(1,10,1):
        if j <= i:
            print("%d*%d=%d"%(i, j, i*j), end="\t")
            if i == j:
                print('\n')

a = [1, 2]
b = [3, 4]
a.extend(b)
a.insert(4, 3)
print(a, '\n', b)

