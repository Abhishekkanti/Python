
n = int(input())
arr = list(map(int,input().rstrip().split()))

arr.reverse()
for e in arr:
    print(e,end=" ")
