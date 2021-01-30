import random
from typing import Any, Union

print("Welcome to my game!")
x = int(input("请输入：（剪刀 0，石头 1，布 2)\n"))
y = random.randint(0, 2)
if y == 0:
    print("电脑出剪刀\n")
elif y == 1:
    print("电脑出石头\n")
else:
    print("电脑出布\n")
if x == y:
    print("平局，请重新开始：")
elif x - y == 1 or x - y == -2:
    print("Win!!!!!")
else:
    print("You lose!")

