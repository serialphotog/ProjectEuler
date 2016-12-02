sum_of_squares = 0
square_of_sums = 0

for i in range(1, 101):
	square_of_sums += i 
	sum_of_squares += i*i
square_of_sums *= square_of_sums
difference = square_of_sums - sum_of_squares
print(difference)