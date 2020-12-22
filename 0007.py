import math
def is_prime(number):

	for i in range(2,int(number)):
		if(number % i == 0):
			return False
	return True	
	
find_all_primes = False
number = 2
primes = []
while(find_all_primes == False):
	if is_prime(number):
		primes.append(number)
	if(len(primes) == 10001):
		print("10001 prime is: ", number)
		break
	number = number + 1
#print (primes)