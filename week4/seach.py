import random
l =[]

for i in range(1000):
    l.append(random.randint(1,1000))

l=[2001,1990,1981,1985,1988,1999]

n=0
while(n>-1):
    print("Enter a number, type -1 to exit:")
    n=int(input())
    flag=0
    for i in range(len(l)):
        if (n == l[i]):
            print("Hip Hip Hurray, element found")
            flag=1
            break;
    if (flag==0):
        print("Element not found")
