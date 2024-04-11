

from itertools import product

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

op = list(product(L1,L2))

for i in op:
    print(i,end=" ")