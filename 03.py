# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

target = 600851475143
largest = 1
d = 2

while target > 1:
	while target % d == 0:
		if d > largest: largest = d
		target /= d
	d += 1
	if d*d > target:
		if target > 1 and target > largest: largest = target
		break

print(largest)