
a = int(input())
setA = set(map(int,input().split()))

b = int(input())
setB = set(map(int,input().split()))

print(len(setA.union(setB)))
