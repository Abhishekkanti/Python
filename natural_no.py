
import sys

t = int(input().strip())
for i in range(t):
    sum = 0
    num = int(input())
    for a in range(num):
        if( a%3==0 or a%5==0):
            sum = sum + a
    print(sum)

        
def natural_num(a):
    sum = 0
    if(a%3==0 or a%5==0):
        sum+=i
    