# write function to find average of list
def avg(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum/ len(l)

x = [4,3,2,2]
print(avg(x))
