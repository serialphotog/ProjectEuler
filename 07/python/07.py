import itertools

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
print(next(itertools.islice(primes, 10000, None), None))