# immutable and muttable have diffrent copy staragies and both work diffrently
# assigment operator is =

d = { 'a':1,'b':2,'c':3 }

# The assigment operator can be used to copy immutable objects
# such as u assign
# here `y` is refering to `x` as 10
x = 10
y =  x
x = 100
print(x) # 100
print(y) # 10
#^ here `y` value din't changed as its `immutable` strings
# as `y`  is just a copy of x's object.

# The assignment operator cannot be used to copy mutable objects.
d_copy = d   # now both d & d_copy are exactly same
d_copy['a'] = 10
print('1. d_copy changes',d_copy) # {'a': 10, 'b': 2, 'c': 3}
print('2. d changes',d) #  {'a': 10, 'b': 2, 'c': 3}
# as u see unfortunatly both d and d_copy are changed. and no one want there old
# dicct to be changed like that. and its a problem.

# since  dict. is a mutable object its behave this way

# SOlUTION. we can copy mutable object via `copy` method or `dict` method.

# Copy dict. using `copy()` method
# Syntax : dict_nameNew = dict_nameOLD.copy()
# the dict_nameNew and dict_nameOLD entirely diffrent dict.
# changes made to any of the dict. wont' be reflected to other.
d_copy = d.copy() # {'a': 10, 'b': 2, 'c': 3}
# both are same d_copy is a copy of dict d .
# changes made to d_copy won't be reflected to dict d


# Copy dict using `dict()` method.
# Syntax : dict_nameNew = dict(dict_nameOLD)
# its same as `copy()` method
d_copy = dict(d) # {'a': 10, 'b': 2, 'c': 3}
