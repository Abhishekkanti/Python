


lst = [ ]
sl = []
for _ in range(int(input())):
	name = input()
	score = float(input())
	
	x = [name,score]
	lst.append(x)
	sl.append(x[1])

b = sorted(list(set(sl)))[1]

for a,c in sorted(lst):
	if c == b:
		print(a)



