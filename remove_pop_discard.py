
n = int(input())
s = set([int(x) for x in input().split()])

totalcmd = int(input())
for i in range(totalcmd):
    cmd = list(input().split())
    if(len(cmd) == 1):
        s.pop()
    elif(cmd[0] == "discard"):
        s.discard(int(cmd[1]))
    elif(cmd[0] == "remove"):
        s.discard(int(cmd[1]))

print(sum(s))

