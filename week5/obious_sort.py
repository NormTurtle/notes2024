# write funciton to sort the list

def minimum_on_list(l):
    less_ = l[0]
    for i in range(len(l)):
        print(i,"isst")
        if l[i]<less_:
            less_ = l[i]
            print(less_,"1st")
    return less_

def obvious_sort(l):
    newl_ = [  ]
    while len(l)>0:
        less_ = minimum_on_list(l)
        newl_.append(less_)
        l.remove(less_)
    return newl_


l = [1,4,2,6,7,8,5,9]
print(obvious_sort(l))
