import random

set=[]
n = random.randint(2,5)
for i in range(n):
    print(i)
    set[i] = random.randint(0,100)

print(set)