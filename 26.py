
n = int(input())

for i in range(n):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    
    except ZeroDivisionError as e:
        print('Error Code: ' + str(e))
    
    except ValueError as e:
        print('Error Code: ' + str(e))