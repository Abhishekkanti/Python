
def print_1_n(n):
	if n == 0:
		return
	print_1_n(n - 1)
	print(n)
	return

def print_n_1(n):
	if n == 0:
		return
	print(n)
	print_n_1(n -1)


print_1_n(10)

print_n_1(10)

