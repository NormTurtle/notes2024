# Dict_comphension = { key : exprsesion for (key,value) in dict_name if condition}

_dict = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5 }
comp_dict = {key : int(val)+1 for key,val in _dict.items() }
print(comp_dict)
# {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}

#turn super hero names to correct and the thigns they do
# using list-commprehension

d = {i:(i**2) for i in range(1,5)  }
# {1: 1, 2: 4, 3: 9, 4: 16}

ages = [ 10,30,52,12,87,100 ]
age_sort = {age:("Young" if age < 40 else "Old") for age in ages }
# {10: 'Young', 30: 'Young', 52: 'Old', 12: 'Young', 87: 'Old', 100: 'Old'}


old_price = {
        'atomic_habit' : 10,
        'compund_effect': 12,
        'do sheep dream of android' : 8
        }
bill_2_ruppe = 0.82

# u need to use `else NONE` as a placeholder idk why exclusive to Dict_comphension
new_price = {k:(v*bill_2_ruppe if v != 10 else None) for k,v in old_price.items()}
# {'atomic_habit': None, 'compund_effect': 9.84, 'do sheep dream of android': 6.56}
