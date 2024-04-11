

def average (array):
    s = set(array)
    avg = sum(s) / len(s)
    return avg

n = int(input())
arr= list(map(int, input().split()))
print(average(arr))


