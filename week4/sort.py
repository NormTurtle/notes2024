# # u can just do the this thing V
# l = [4,1,3]
# l.sort()
# print(l)  # [1,3,4]

# but ^^ is for normie
# lets to this HARD WAY

l = [4,6,3,7,5,32,8,6,1,24,6,9,2,4,10]
Sorted_list = [  ]
while(len(l)>0):
    m = l[0]
    for i in range(len(l)):
        if l[i] < m:
            m = l[i]
            # print(m)
    Sorted_list.append(m)
    l.remove(m)

print('sort',Sorted_list)
print('l',l)
