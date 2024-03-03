# LOOPING
# for x in range(n)
# for a in  range(5):
#     print(a)
#> here a is varible which will be increamten over the time going through loop
# range is varible of how much somethign to go for
# : <CR> tell what do each time in range(n)

# `range` teakes 3 arguments as (START,END,STEP)
# default value for `END` & STEP  is 1 for START its 0

# #Q.1 print even if even , print odd if odd
# n = int(input("enter number to go thorugh to check wether its even or odd : "))
# for n in range(10):
#     if (n%2 ==0 ):
#         print(n,'is even')
#     else:
#         print(n,'is odd')

#Q.! sums the given digits

# n = int(input("enter a number to be summed digits : "))
# ans = 0
# for x in range(n):
#     ans = ans + x
#     print(ans)

# #Q.! find the factorial
# n = int(input("enter a number to be summed digits : "))+1
# #^> added + 1 becuase i skip the first number 0 which makes it 1 less
# for the counter part of that i have to add 1
#^ i removed 0 becuase anywher its multiplicaiotn makes everythign 0
# ans = 1
# for x in range(n):
#     if x > 0:
#         ans = ans * x
#         print(ans)


#Q.! write tabels of the giivne number
#> u can define range interval using range(START,END) here end is non-inclusive

# num = int(input("Enter number to give its Table : "))
# for i in range(1,11):
#     ans = i * num
#     print(num,"X",i,"=",ans)
#


#Q.! `for` without `range`
#^> u can do that with help of kinda of string slicing
# word = "String"
# for x in word:
#     print(x)
# >> S t r i n g
#^ it outpts each letter on new line
# its like `foreach` from CT go over each letter provided


#Q.! give all odd number reverse order from 1-20
for i in range(21,0,-2 ):
    print(i)
#v OUTPUT
# 21
# 19
# 17
# 15
# 13
# 11
# 9
# 7
# 5
# 3
# 1


# Q.! factorial using for loop
# using range we are making it being negative each time it iterate
fact = 1
for i in range(5,1,-1):
    fact = fact * i
    print(fact)
