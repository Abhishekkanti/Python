
s= input()

str = s.split()

print(str)
print(type(str[1]))

int_list =[ ]

for i in str:
	int_list.append(int(i))

print(int_list)
print(type(int_list[1]))

n = [int(i) for i in input().split(',')]