# making a empty list
a = [  ]
#^here a is a empty list

# `append`to the list
a.append([ 1,2,3 ])
a.append([ 4,5,6 ])
print(a)

# `remove` form lsit
# a = a.remove(2) # will remove first occurance of 2

# u can contain list within list within list ..... on and on.
# list = [[1, 23, 4], [23123], [], [123134]]

# `list slicing` works same as string slicing but it treat list as on
print(a[1]) # will print the 2nd list/element of list a
# [ 4,5,6 ]

# `list slicing ` on the list of list's element
print(a[0][1]) # will print the list of list's second element
# 2
