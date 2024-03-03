m=int(input('Enter number of row in first matrix m= '))
n=int(input('Enter number of column in first matrix (same as number of row in 2nd) n= '))
p=int(input('Enter number of column in 2nd matrix p= '))

A=[]
print('Enter elements of first',m,'x',n,'matrix')
for i in range(m):
  X=[]
  print('This is row number',i)
  for j in range(n):
    X.append(int(input()))
  A.append(X)
#author manish
B=[]
print('Enter elements of Second',n,'x',p,'matrix')
for i in range(n):
  X=[]
  print('This is row number',i)
  for j in range(p):
    X.append(int(input()))
  B.append(X)

#multiplication starts
mult=[]
for i in range(m):
  X=[]
  for j in range(p):
    element=0
    for k in range(n):
      element+=A[i][k]*B[k][j]
    X.append(element)
  mult.append(X)

print('A=',A)
print('B=',B)
print('AxB=',mult)
