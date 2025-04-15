from random import random
import sys

assert len(sys.argv) == 2, "Wrong nargs."

n: str = sys.argv[1]
mylist: list = [None] * int(n)

for i in range(int(n)):
    rand: float = random()
    mylist[i] = rand

print(max(mylist))
print(min(mylist))