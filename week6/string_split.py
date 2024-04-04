# `split()`
s = "hello my name is kureha" # words are sperated with space here
# Syntax: string.split(SEPARATOR,MAXSPLIT)
# SEPARATOR = thing to consider for as sep. default :  " " a space only. can't be empty ""
# MAXSPLIT = how many split to perform. default : -1 , perform all occurance
# create a list of words in provided string
# e.g

print(s.split()) # ['hello', 'my', 'name', 'is', 'kureha']
print(s.split(" ",2 )) # ['hello', 'my', 'name is kureha']
#^ see the list created

# Create list using `.split()` method via input()
list1 = input("enter number with space for list: ").split()
print(list1)  # ['10','20','30']  based on input


