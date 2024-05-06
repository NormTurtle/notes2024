last = 0
n = 0
l = []
while not n > 100 :
    n += 1
    for i in range(2,10,-1): # from 2 to 10
        if n % i == 0 :
            last = n
            l.append(n)

print(last)
print(l)
