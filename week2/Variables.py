# u can only give alphanumeric,_(underscore)only symbol as variable name
# u can start a variable with number `1y = yes` is invalid
# u can start with _ undersocre as `_1y = yes` is valid
# u can give multiple vallues to vairable
a,b = 1, 3
print(a,b)
# or assign multiple variable same value
y = x = a = b = 10
print(y,x,a,b)

# update a vairable | transverse |
x,y = 1,2
print(x, y )
x,y = y ,x
print(x, y )


# delte a variable
a = 10
print(a)
del a

# variable name are CaseSensetive
# u can't use operator names ( print , if , in , and , or  ) for variable names
