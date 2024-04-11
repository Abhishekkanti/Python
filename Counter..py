from collections import Counter

s = int(input())
sizeOfshoes= list(map(int, input().split()))
n = int(input())

profit = 0
for i in range(n):
    size , price = map(int , input().split())
    if size in  sizeOfshoes:
        profit += price
        sizeOfshoes.remove(size)
print(profit)
    