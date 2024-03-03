# dot product is multipactoin and them sum of them

# Q.! find the dot product of 2 vector
v1 = [1,1,1]
v2 = [2,3,1,]

sumVector = 0
for i in range(len(v1)):
    sumVector = sumVector + (v1[i]*v2[i])

print(sumVector)  # 6
