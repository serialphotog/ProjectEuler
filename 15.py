from math import factorial

# Implementation of n choose k
def combinations(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

def paths(gride_size):
	return combinations(gride_size*2, gride_size)

print(paths(20))