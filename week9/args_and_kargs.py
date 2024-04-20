# *args -> tuple
# collect all positional arguments that are pass into function as  single tuple.
# hanndy when u have so many arguments passwed to function.

# 1.
# here *args can be any value as *foo
def add(first,second,*args):
    print(f'all *args values: {args}',)
    for i in args:
        print('args vales : ',i)
    return first+second
# first+second+args

print(add(1,2,3,4,5,6,7,8,9,10))
# print(add(1,2,3,4))

# 2.
# **kwargs -> dict
# collect keywords arguments into dictionary

def idk(**kwargs):
    print(kwargs)


print(idk(name='omi',id='chan'))
#output :  {'name': 'omi', 'id': 'chan'}

# 3.
# both *args and **kwargs
#       ^(tuple)  ^(dict)

def args_and_kwargs(*args,**kwargs):
  print(f'all args value \n \t{args}')
  print(f'all args value \n \t{kwargs}')



print(args_and_kwargs(1,2,3,4,name='omi',id='chan'))
