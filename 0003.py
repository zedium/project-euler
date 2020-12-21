import math

original_number =600851475143
number = int(math.sqrt(original_number))

primes = []	 

def is_prime(number):

	for i in range(2,int(math.sqrt(number))-1):
		if(number % i == 0):
			return False
	return True	

for i in range(2,number):
	if(is_prime(i)):
		primes.append(i)
		
for prime in reversed(primes):
	if(original_number%prime==0):
		print("number is: ", prime)
		break