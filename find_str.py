#def str_find(string,sub_str):
#    count = 0
#    for i in range(len(string) - len(sub_str) + 1):
#        if string[i:i + len(sub_string)] == sub_string:
#            count += 1
#    return count
#    
#word = input().strip()
#sub_string = input().strip()
#count = str_find(word,sub_string)
#print (count)

def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            flag = 1
            for j in range(0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag = 0
                    break
            if 1 == flag:
                count += 1
    return count