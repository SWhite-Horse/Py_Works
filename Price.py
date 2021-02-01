import random
To_Do = [["虞姬", 888], ["貂蝉", 1888], ["克拉拉", 18888], ["林志玲", 88888], ["迪丽热巴", 99999]]
for Did in To_Do:
    x = To_Do.index(Did)
    print(x+1, end='\t')
    for i in To_Do[x]:
        print(i, end='\t')
    print('\n')
Did_Choose = []
num = 0
Pay = 0
while num < 5:
    Did_Choose.append(int(input("请问你要干辣锅：")))
    if Did_Choose[num] == 9:
        Did_Choose.pop()
        break
    Pay += To_Do[Did_Choose[num]-1][1]

    num += 1
print("你想嫖", end='')
for i in Did_Choose:
    print(To_Do[i-1][0], end=",")
print("一共要花：%d"%Pay)
