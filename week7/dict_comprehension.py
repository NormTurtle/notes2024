# Dict_comphension = { key : exprsesion for (key,value) in dict_name if condition}

_dict = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5 }
comp_dict = {key : int(val)+1 for key,val in _dict.items() }
print(comp_dict)
# {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
