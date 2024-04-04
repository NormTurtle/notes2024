def digit_count(n):
    D = {}
    for i in range(10):
        D[i] = 0
    for j in range(1,n+1):
        for k in str(j):
            D[int(k)]+=1
            print(k)
    return D

n = int(input("enter num: "))
print(digit_count(n))
