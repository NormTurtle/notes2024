l = []
for i in range(1,1000+1):
    l.append(pow(i,i))


sumed = str(sum(l))
print(sumed[-10:])  # print last 10 digits . starting from last 10th digit to end


# output:
# 9110846700
