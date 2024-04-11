
t = int(input())

#for i in range(t):
#    even = ""
#    odd = ""
#    #word = list(map(str, input()))
#    word = str(input())
#    for j in word:
#        if(word.index(j)%2==0):
#            even = even+j
#        else:
#            odd = odd+j
#    print(even,odd)

for i in range (0 ,t):
    S = input()
    print(S[0::2] + " " + S[1::2])