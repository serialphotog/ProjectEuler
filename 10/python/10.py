import itertools as it

# Taken from problem #7
def gen_primes():
	D = {}
	q = 2

	while 1:
		if q not in D:
			yield q
			D[q*q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p+q, []).append(p)
			del D[q]
		q += 1

primes = gen_primes()
print(sum(it.takewhile(lambda x: x < 2000000, primes)))