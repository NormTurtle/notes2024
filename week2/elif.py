# Else-if | ELIF | Eles + If 
# run this command if above if statement is not matched
# ELIF statement takes account for previous if statement
# as if 5 < 10 : elif 1 < 5  , it can remerbe previous stats.
# ^ here elif know that 5 < 10 from if statement
# ELIF  is like ` if XXX and XXX ` combined

# Q.! find the given if number end with 0 or 5 or any other number? using elif
#^> logic is that number eding with 0 e.g 100 must be divisible by 10
#^> number ends with 5 e.g 45 must be divisible by 5

num = int(input("give number to check if its ends with 5 or 0:"))
if (num % 10 == 0):
    print(0)
elif (num % 5 == 0):  # used ELIF instead of IF so it check the above
# line condition is not met or else i would have 2 output 0,5
#^ here ELIF is simpler version of if (num % 10 == 0 and num % 5 == 0)
    print(5)
else:
    print("other")



# Q.! Find the grade of score from 0 to 100 as
# A  >= 90
# B = >=80 and < 90
# C = >=70 and < 80
# D = >=60 and < 70
# E = <60
mark = int(input("Enter marks:"))
if(mark >= 90):
    print("A")
elif(mark >= 80):  # if above condition isn't matched do this on remaing parts
    print("B") # here ELIF is aware of > 90 part even we din't told it
# ^> if (mark >= 80 and mark  < 90 ):
# this is same as above ELIF statement
elif(mark >= 70):
    print("C")
elif(mark >= 60):
    print("D")
else: print("E")
