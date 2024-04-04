# make funciton to make any dimeson of matrix


# def make_mat(dimeson):
#     return [[0 for i in range(dimeson)] for j in range(dimeson)]
#
# print(make_mat(9))


# a = [[0,0,0],[0,0,0],[0,0,0]]
# print(len(a))



# # wriet funciton to sum till n
# def sum_(x):
#     total = 0
#     for i in range(x):
#         total = total + (i+1)
#     return total
# print(sum_(100))

# function for factorial
def fac(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
        print(fact,"facccc")
    return fact
print(fac(5))
