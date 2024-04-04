# Mutable = change/update and remove/del
d = { 'a': 1,'b': 2, 'c': 3 }

# Changing Value using Key names
# Syntax :  dict_name[key] = value
# will update that specifed `key` with specifed `value`
d['a'] = 100   # value of key a is now 100 from 1
d['d'] = 5   # adding new value using key name method
print('1. dict[key]= value method :',d) # {'a': 100, 'b': 2, 'c': 3, 'd': 5}
# also dict `d` is udpate by this

# Changing Value using `.update()` method
# Syntax : `dict_name.update(dictionary)`
# `dictionary` is a parameter. as {key:value}
d.update({'a':1})  # this way u can update any value or append new valeu
d.update({'f':6})  # adding new value
print('2. dict_name.update() method : ',d) #  {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'f': 6}

# Remove value using `pop()` method
# Syntax : dict_name.pop(key)
# remove item using *key* of the *item*
# returns the delted item's value
# item means key:value pair combined
d.pop('a') # 1  # 1 is the value of key 'a'
print('3. Removed key \'a\':1 using pop() :',d) # {'b': 2, 'c': 3, 'd': 5, 'f': 6}

# Remove item using `popitem()` method
# Syntax : dict_name.popitem()
# if none item is given in argument it deletes the last item of dict.
# returns Removed as tuple | a tuple is a limited list with round bracket()
d.popitem() # ('f', 6)  # the last item in the dict.
print('4. Removed itme using popitem() : ',d) # {'b': 2, 'c': 3, 'd': 5}


# Remove an item using `del` keyword
# never returns anything
# Syntax : del dict_name[key]
del d['b'] # no output
print('5. Removed item using `del` keyword : ',d) # {'c': 3, 'd': 5}

# remove a entire dict. using `del` keyword
# Syntax : del dict_name
del d
print('6. deleted whole dict using `del` keyword : ')
# print(d)  # Name Error d is not defined

# empty a dict. using `clear()` method
# Syntax : dict_name.clear()
# Empties the  dictionary
d = {'a':1,'b':2}
d.clear()  # None
print(d) # {}
