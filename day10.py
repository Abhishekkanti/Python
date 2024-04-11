

n = int(input())
binary= []
binary.extend(bin(n))

res = 1
#for el in binary:
#    if binary[el] == 1:
#        if binary[el] == binary[el +1]:
#            res.append(binary[el])
#       

#print(len(res))

for i in range(len(binary) - 1):
    while binary[i] == binary[i + 1]:
        res += 1
        #print res * "0"
        break
    #else:
     #   res = 1
        #print counter * "1"
print(res)
#print(binary)