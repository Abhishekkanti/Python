


n = int(input())
std_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    std_marks[name] = scores 

qry_name = input()

output = list(std_marks[qry_name])    
per = sum(output)/len(output)
print("%.2f" % per)
		
		