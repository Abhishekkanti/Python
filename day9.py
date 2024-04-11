
n = int(input())
book = dict()
for _ in range(n):
    name, num = input().split()
    book[name] = num

while True:
    try:
        find = str(input())
        if find in book:
            print(find+"="+book[find])
        else:
            print("Not found")
    except EOFError:
        break
