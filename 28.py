

n = int(input())
arr = input().split()
print(all([ int(i) > 0 for i in arr]) and any([ j == j[::-1] for j in arr]))

