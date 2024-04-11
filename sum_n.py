

def sum_n(n):
	if n == 0:
		return 0
	smallOutput = sum_n(n - 1)
	output = n + smallOutput
	return output
	
print(sum_n(5)) 
	