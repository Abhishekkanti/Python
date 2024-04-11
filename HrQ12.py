# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

odr = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    odr[item] = odr.get(item, 0) + int(price)
for item, price in odr.items():
    print(item, price)