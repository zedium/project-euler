
#from array import *



cols, rows = (20,20)

arr = [[0 for i in range(rows+1)] for j in range(cols+1)]



for i  in range(cols+1): 
	arr[0][i]=1
	arr[i][0]=1
	

for i in range(1,cols+1):
	for j in range(1, rows+1):
		arr[j][i] = arr[j][i-1]  + arr[j-1][i]
		

print("Result is :", arr[rows][cols])