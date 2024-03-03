# cerating random list from  1 - 365
# checking if the random list of have soem thign in common.
import random
x = [  ]
for i in range(30):
    x.append(random.randint(1,12))
x.sort()   # sort the list
print(x)
# print(x)
