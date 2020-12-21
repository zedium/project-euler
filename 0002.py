


prev_number = 1
next_number = 1
result = 0
while next_number < 4000000:
	temp = next_number

	if next_number % 2 == 0:
		result = result + next_number
	next_number = next_number + prev_number
	prev_number = temp
	

	
print(result)