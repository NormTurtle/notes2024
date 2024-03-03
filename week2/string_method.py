# methods to work with strign in python
# Manipulation
print("Manipulation")
# x.lower() # turn lettes to lowercase
# x.upper() # turn lettes to uppercase
# x.capitalize() # turn first letter of sentece to uppercase
# x.title() # turn first letter of each word to uppercase
# x.swapcase # invert the Case of each letter

t = "A wOrd WiTH a WeIrd chaRAcTers"
lowercase = t.lower()
print("lowercase",lowercase)
uppercase = t.upper()
print("uppercase",uppercase)
captil = t.capitalize()
print("capitalize",captil)
title = t.title()
print("Title",title)
swap = t.swapcase()
print("swapcase",swap)

print("is t","totaly lowercase",t.islower())
print("is t","totaly uppercase",t.isupper())
print("is t","totaly captil",t.isdecimal())

print("is lowercase","totaly lowercase",lowercase.islower())
print("is uppercase","totaly uppercase",uppercase.isupper())

# checking
print("Checking")
# x.islower # return true if string is lowercase
# x.isupper # return true if string is uppercase
# x.istitle # return true if string is in Title Form
t = "TEST FOR THE CHECK"
checkLower = t.islower()  # False
print(checkLower)
checkUpper = t.isupper()  # True
print(checkUpper)
checkTitle = t.istitle()  # False
print(checkTitle)

# x.isdigit # True if all the letter are number/digits
# x.isalpha # True if all the letter are Alphabates
# x.isalnum # true if contains `numbers and alphabates` only
# >>  means if there is symbol it will be output would be False
t = "1000abc"
checkDigit = t.isdigit() # False
print(checkDigit)
checkAplha = t.isalpha() # False
print(checkAplha)
CheckAlNum =  t.isalnum() # True
print(CheckAlNum)

# Trimming
# x.strip(XXX) # provided XXX get removed from the string
# x.lstrip(XXX) # provided XXX pattern got removed from the LEFT side only
#^>> no Change on right by lstrip
# x.rstrip(XXX) # provided XXX pattern got removed form Right side only
#^>> no Change on left side by rstrip
t = "----amasogi----"
Trim = t.strip("-")  # amasogi
print(Trim)
TrimLeft = t.lstrip("-") # amasogi----
print(TrimLeft)
TrimRight = t.rstrip("-") # ----amasogi
print(TrimRight)

# End/First pattern checking
# ^>> in python most thing are CaseSensetive as this checking are also
# x.startswith(XXX) = True if String pattern start with provided (XXX)
# x.endswith(XXX) = True if String pattern ends with provided (XXX)
t = "kiriha-san"
CheckFirst = t.startswith("kir") # True
print(CheckFirst)
CheckLast = t.endswith("an")    # True
print(CheckLast)

# Indexing
# x.count(XXX)  # return how many time a somethign appeared
# x.index(XXX)  # looks for position number of XXX
# x.replace(XXX,YYY) # substidute pattern XXX with YYY
# ^>> if u did x.replace("t","o") # it will change ALL occurance of `t` with `o`
t = "Amasogi are BAD"
CheckCount = t.count('a') # 2
print(CheckCount) # means  `a` occure 2 times
CheckIndex = t.index('D') # 14
Replaced = t.replace("BAD", "GOOD") # Amasogi are GOOD
print(CheckIndex) # means `D` in `t` is at 14th position
print(Replaced)
