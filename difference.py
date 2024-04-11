m = int(input())
setM = set(map(int,input().split()))

n = int(input())
setN = set(map(int,input().split()))

list1 = list()

for i in setM:
    if i not in setN:
        list1.append(i)
        
for j in setN:
    if j not in setM:
        list1.append(j)

list1.sort()

for i in list1:
    print(i)