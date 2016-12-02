# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b / gcd(a, b)

l = lcm(19, 20)
for i in range(18, 1, -1):
	l = lcm(i, l)

print(l)