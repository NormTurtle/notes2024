# define a functoin which takes input as pay,discoutn
# # and return the amount re
# def dis(amt, disc):  # defining functoin
#     dis = amt - (amt * (disc / 100))
#     return dis
#
#
# x = int(input("give amount: "))
# y = int(input("give discount: "))
# # print(int(dis(x, y)) + 10)
# print(dis(x, y) + 10)


# function on list
# minimum of list
#def l_min(x):
#    chota = x[0]
#    for i in range(len(x)):
#        if x[i] < chota:
#            chota = x[i]
#    return chota
#i = [20,7,23,2,2,2,2,2,2,2,6, 2, 3,1]
#print(l_min(i))
# find maximum of list
def Big_list(x):
    bada = x[0]
    for i in range(len(x)):
        print(i)
        if (x[i] > bada):
            bada = x[i]
    return bada


x = [1,4,7,2,4,6,7,88,2,4,23,4,7,7,88,2,2,2,233,13,19999]
Big_list(x)
