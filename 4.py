def isPalindrome(num):
	original = str(num)
	reverse = original[::-1]
	if original == reverse: return True
	return False

def main():
	largest = 0

	for i in range(100, 999): # num 1
		for j in range(100, 999): # num 2
			product = i*j
			if isPalindrome(product) and product > largest: largest = product

	print(largest)

main()