

number = 1;
found = False

while(found == False):
	
	counter = 0
	
	for i in range(1,21):
		if((number % i) ==0):
			counter = counter +1
		else:
			break

	if(counter == 20):
		print("The number is: ", number)
		found = True

	number = number + 1
	
	
