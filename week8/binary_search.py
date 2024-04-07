import time as t
l = list(range(30000))

def obvious_search(l,k):
  for i in range(len(l)+1):
    if i == k:
      return print("TRUE")
  return print("FALSE")


k = 299999999

def binary_searach(l,k):
  begin,end = l[0], l[-1]
  while(begin <= end):
    m = (begin+end)//2
    if l[m] > k:
      end = m-1
    elif l[m]<k:
      begin = m + 1
    elif m == l[m]:
      return print("TRUE",)
  return print("FALSE",)


a=t.time();obvious_search(l,k) ;b=t.time();print('time to run obvious_search',b-a)

a=t.time();binary_searach(l,k);b=t.time();print('time to run binary_searach',b-a)
