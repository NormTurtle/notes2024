# Please see ./dict_mutable.py for more on methods
# dictionary contain key:value pair in a {} curly bracket
# dictionary keys are the unique value
# View Object : are the list getting update each time some operation are performed
# access values using *keys names*
# syntax : dict_name[key]
d = { 'a': 1 , 'b': 2 , 'c': 3  }
print(d['c']) # 3

# access values using *get(key)* the safe way if not found wont throw error
# syntax : dict_name.get(key)   # return value else return NONE
print(d.get('c'))  # 3

# access using *keys()*
# Return a *view object* containing key as a list.
# * View object * reflects any changes done to the dictionary.
# mean gives a update list each time some operation run on dict.
# syntax : dict_name.keys()
d_keys = d.keys()  # now d_keys contain all the `keys` of dict `d`
print(d.keys()) # dict_keys(['a', 'b', 'c'])

# access value using `values()` method
# Return a * view object * contain value as list
# syntax : dict_name.values()
d_values = d.values()
print(d_values) # dict_values([1, 2, 3])


# access `item` using items() method
# a * Item * is pair of key:value.
# if ur interested in key:values pairs then u should `item`
# `items()` method also Return * view object * as a list . * view object * is update also
d_item = d.items()
print(d_item) # dict_items([('a', 1), ('b', 2), ('c', 3)])
