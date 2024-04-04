# zip function print ITEM with tuple of two iterable

user = ['bat','spider','iron']
passw = ['bat@123','strongpass','hard1@32']

zep = zip(user,passw)
print(type(zep))
for i in zep:
    print(i)

# <class 'zip'>
# ('bat', 'bat@123')
# ('spider', 'strongpass')
# ('iron', 'hard1@32')


# you can also do typecastign
zep = dict(zip(user,passw))
print(type(zep))
# <class 'dict'

for key,value in zep.items():
    print(key+" : "+value)

# bat : bat@123
# spider : strongpass
# iron : hard1@32
