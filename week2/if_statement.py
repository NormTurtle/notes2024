#IF XXX : /t else
# you want to visit aki`h` but you have comply with age limit
#^> make something that can check your age
#       Indentaion is important in IF statements
CurrentYear = 2024
print("U wanna watch some badakte hue japani cartoon jalchitr?")
BirthYear = input("Please enter your Year of birth to confirm:")
age = CurrentYear - int(BirthYear)
if abs(age) > 18:
    print("Your allowed to enter 😼\n As", age, "is above 18")
else:
    print(age,"is Not old enough, Now U have 2 option \n 1. Left this place \n 2. or click that button to confirm your age ")
    print("thsi is part of else state")
print('This is not a part of else state')





# Q.! check wether the given number is even or odd
#> here im going to use logic of modulo with 2
# if a number is divisible by 2 then its even. if not then odd

# num = int(input("enter a number to check if its even or odd:"))
# if num % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
