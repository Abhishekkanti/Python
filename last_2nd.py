# cook your dish here

l = []
op = []

for _ in range(int(input())):
    x,y,z = map(int,input().split())
    l.append(x)
    l.append(y)
    l.append(z)
    op.append(sorted(set(l))[-2])
    l.clear()

for i in op:
    print(i)