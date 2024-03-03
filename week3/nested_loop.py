# u can create nested loop where inside is
# going thorough each value of the loop above it
w = "ab"
n = "12"
for i in w:
    for a in n:
        print(a,i)
# ^ OUTPUT
# 1 a
# 2 a
# 1 b
# 2 b
#^ u see that repeated pattern that is becuase of nested loop
