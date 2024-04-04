# write a funcion to sum n values of non-negative integers

# via `Recursion`
def sum1(n):
    if n == 0:
        return 0
    else:
        return n + sum1(n - 1)
# hit the base here `0` by n beign negative n times.
#when hit base 0 . starts adding up things to n
print(sum1(int(input("\t\t\t\t\t:")))) # tabs make it look cool


# via `non-Recusion funcion`
def sum2(x):
    value = 0
    for i in range(x+1): # added 1 because range starts form 0
        value += i
    return value
# increamenting with all value of non-negative.
n = 10
print('sum2 answer',sum2(n))  # 55



# via `mathematical` formula (n*(n+1)/2)
def sum3(n):
    return n * ( n + 1 ) / 2

n = 5
print("sum3 : ",sum3(n))  # 15.0
