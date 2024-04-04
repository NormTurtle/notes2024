r1 = [3,2,2]
r2 = [4,1,3]
r3 = [1,3,1]
c1 = [1,2,1]
c2 = [3,1,1]
c3 = [3,1,2]
A = []
B = []
A.append(r1)
A.append(r2)
A.append(r3)
B.append(c1)
B.append(c2)
B.append(c3)
blank_ = [0,0,0]
mat_dim = 3   # 3X3
dot_mat = [  ]  # A X B
dot_mat.append(blank_)
dot_mat.append(blank_)
dot_mat.append(blank_)
print(dot_mat)
for a in  range(mat_dim):
    for b in  range(mat_dim):
        for c in range(mat_dim):
            dot_mat[a][b] = dot_mat[a][b]+A[a][c]*B[b][c]

print(dot_mat)

import numpy
A = numpy.mat(A)
B = numpy.mat(B)
print(A*B)
