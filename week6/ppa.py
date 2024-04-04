def maxval(a, b, c):
"""
    compute the maximum among three numbers
    Arguments:
        a, b, c: integers
    Return:
        max_of_three: integer
"""
    list = [a,b,c]
    big = 0
    for i in list:
        if i > big:
            big = i
    return big



print(maxval(1,20,3))
