# `def` means to define a function.
# if ur using a same code repeatedly, u can use funciton as
# small block to be used over & over again

# def function_name(parameter):
#   # `indentation` is important
#   """
#   Docstring :  brief info of function
#   """
#   Funciton_body: statement of sysntax code
#   return $value

# u can call function by `function_name`
# e.g
def foo():
    print("hello world")
# here i call it by removing it from indentation
foo() # output: hello world

# Example function of sqare a integer
def Sqare(i):
    """
    this functino turn integer to sqare
    """
    return (i ** 2)

print(Sqare(2))  # output: 4
print(Sqare(4)) # output: 16
Sqare(10) # output: 100  | but its not getting printed as its not called by print()
