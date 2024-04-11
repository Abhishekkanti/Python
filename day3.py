import math
import os
import random
import re 
import sys


def solve(cost, tip,tax):
    tip = (cost*tip)/100
    tax= (cost*tax)/100
    print(round((cost+tip+tax)))
    

if __name__ == '__main__':
    
    mealcost = float(input().strip())
    tip_percent= int(input() .strip())
    tax_percent=int(input().strip())
    solve(mealcost, tip_percent, tax_percent)