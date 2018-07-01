from math import sqrt

# Gets the next triangular number from last
def next_trianglular(last, n):
	return [last+1, n+last+1]

def get_factors(n):
	step = 2 if n%2 else 1
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

last = 2
n = 3
while 1:
	last, n = next_trianglular(last, n)
	factors = get_factors(n)
	if len(factors) > 500:
		break
print(n)