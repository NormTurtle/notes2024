# recursion function means to function calling it self inside the execution
n = 0
def recur_(n):
    n += 1
    recur_(n)
    return n
