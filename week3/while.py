# While is like english word which does somethign till <Condition> match

# # Demonstarting While with a game of guess who is rich
# maiden = input("\t\tWho is rich ? \n a = kureha \n b = suzutsuki \n c = usami \n d = narumi \n e = subaru \n \t\t Type here a|b|c|d: ")
#
# while maiden != 'b' :
#     print("actually that is wrong answer")
#     maiden = input("Try again \n \t\t\t a|b|c|d : ")
# #^> thsi `while` run untill i pass b as input
# #> whihc will make `maiden = b` hence `while loop` to end
#
# print("That the answer and you won nothing.")
# #> this `print` statement will run after the `while` is done
#
#

# # another problem do factorial with while
#
# n = int(input("enter a num : "))
# if n == 0:
#     print("0 wonrg")
#
# f = n
# while(n>1):
#     n = n - 1
#     f = f * n
#     print(f)
# # print(f)
#

# #Q.! find the number of digit present in integer
#
# a = int(input("enter a num: "))
# digit = 1
# while not (a<9):
#     a  = a // 10
#     digit = digit + 1
#
# print(digit)
# #> here digit is being divied by 10 reducing it each time
# # till its less then 2 digits
#

#Q.1 reverse a number
t = int(input("enter a num: "))
print(t[::-1])
