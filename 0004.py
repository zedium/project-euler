def revers(number):

	result = 0

	while(number>0):
		
		result = (result * 10) +(number % 10)
		number = number // 10
		
	return(result)     
	
arr = []
for i in range(900,999):
	for j in range(900,999):
		if(i*j == revers(i*j)):
			arr.append(i*j)
			
print(max(arr))