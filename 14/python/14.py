def collatz(n):
	count = 0
	while n != 1:
		count += 1
		if n%2 == 0:
			n = n/2
		else:
			n = (3*n)+1
	count += 1
	return count

longest = 0
longest_len = 0
for i in range(2, 1000001):
	chain_len = collatz(i)
	if chain_len > longest_len: 
		longest_len = chain_len
		longest = i
print(longest)