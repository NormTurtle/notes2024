# https://bsc-iitm.github.io/python/ppa/week-5/PPA-8.html

# about fibonacci Sequence


n = 10
def fibo(n):
    if n in [1,2]:
        return 1
    return n-1 + n-2
l = [fibo(i) for i in range(1,n)]
print(l)


#or 


def fibo_(n):
    if n <= 2:
        return 1
    return fibo_(n - 1) + fibo_(n - 2)

print(fibo_(10)) # 55
