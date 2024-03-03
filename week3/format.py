# formating output

# for r in range(5):
#     print(r)
# the problem with above code is that it print on each new line
# what i want conten  on the same line?
#> use formating VV

# for r in range(5):
#     print(r, end = " ")
#^ here i defined the end formater
# there are many naming for formamter in python  like end | sep | start
# `end` takes arugment which separates between diffrent outputs. Default is a new line `/n`
# `end` simply mean what should be comes at end

# print(1,2,3) # this gives spaces between digits but i want something else then <spaces>
# print(100,21,3,123 , sep = "|") # 100|21|3|123

# print("today's date is", end = " ")
# print(23,2,2024, sep = "/")
# #>> today's date is 23/2/2024
#^ here using end , sep both on diffrent line affect eather others
# since they adjacent to each other.

# # `fprint` = formated printing
# var1 = 1
# var2 = 2
# print(f"{var1} and {var2} or {var2+var1}") # 1 and 2 or 3
# # OR
# print("{0} and {1} or {2}".format( var1, var2 , var2+var1)) # 1 and 2 or 3
# # OR
# print("%d and %d or %d" % (var1,var2,var2+var1)) # 1 and 2 or 3
# #^ this method is refred as `String Modulo Operator` , `%d` stand for digit
#

# # print value of pi using formated printing
# pi = 22 / 7
# print(f"Value of pi = {pi}") # 3.142857142857143
# print("Value of pi is {0}".format(pi)) # 3.142857142857143
# print("Value of pi is %f" % ( pi )) # 3.14157   `less output? its limitation of String Modulo Operator`
# #^> `%f` =  float , `%d` = "digit"
# # using `Formate Specifires` : used to modify the output
# # `:.Xf ` stand for print only X digit after decimal
# pi = 22 / 7
# print(f"Value of pi = {pi:.3f}") # 3.141        `output is changed becuase of :.3f` 3 digit after decimal
# print("Value of pi is {0:.2f}".format(pi)) # 3.14
# print("Value of pi is %.2f" % ( pi )) # 3.14

## print Right aligned that thing like pyramid
# print('{0}'.format(1))
# print('{0}'.format(11))
# print('{0}'.format(111))
# print('{0}'.format(1111))
# print('{0}'.format(11111))
#^ code to give below output
# 1
# 11
# 111
# 1111
# 11111
# ANSWER
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
#^ code to give below output
#     1
#    11
#   111
#  1111
# 11111

#^> here `5d` stands for 5 digits also treats spaces as digit
