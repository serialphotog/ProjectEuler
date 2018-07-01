def main():
	LIMIT = 1000

	for a in range(1, LIMIT):
		for b in range(a, LIMIT-a):
			c = LIMIT - (a+b)
			if a+b+c == LIMIT:
				if ((a*a) + (b*b)) == (c*c):
					print("a " + str(a) + " b " + str(b) + " c " + str(c))
					print(a*b*c)
					return

main()