

def pow(x,n):
	if n == 0 :
		return 1
	p = 1
	p = x * pow(x,n-1)
	return p
	
print(pow(4,2))