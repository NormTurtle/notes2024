i = [1, 2, 3, 4, 5, 6, 7, 8, 9]
j = [1, 2, 3, 2, 3, 4, 3, 4, 5]

def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]

def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))

def h(x):
    return x ** 0.5
def pearson(X, Y):
	"""
	Compute the correlation coefficient
    Arguments:
        X: list of float
        Y: list of float
    Return:
        result: float
	"""




X = [float(x) for x in i]
Y = [float(y) for y in j]
