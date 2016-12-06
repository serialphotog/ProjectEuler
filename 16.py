result = 2**1000
result_string = str(result)
total = 0
for char in result_string:
	total += int(char)
print(total)