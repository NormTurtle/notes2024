# When a funcion calles it self with-in it-self
# example by sudarshan sriiyenger
# hyposis: u have to clean 10 vessel.
# u did the worst vessel now u passwed (10-1) = 9 vessel to 2nd guy
# 2nd guy cleaned n-1 (9th)  vessel now he passed it to 3rd guy
# and so on until the vessel is cleaned. like a loop
# e.g :
# Factorial(n) = n * (n-1)
# sum(n) = n + sum(n-1)

# Recursion require `base condition`
# as Recursion is has to stoped or it will run forever.
# here `base condition` is if the last recursion value matches to be 1
# return 1 to it. and stop the funcion and return the original value.

# pro TIP :
# BREAK stop the nearest top level LOOP. not the If statement

# Factorial in recursion
def facto(n):
    if n == 1:
        return 1
    return (n * facto(n-1))

facto(7) # 5040
print('1. Factorial of 5 : ',facto(5)) # 120

# Sum of n int digits using Recursion
def sum_(n):
    if n == 1:
        return 1
    return n + sum_(n-1)
sum_(5) # 15
print('2. Sum of first 10 digit',sum_(10)) # 55
