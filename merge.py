s = input()
k = int(input())


def merge(string,num):
    length = len(string)
    sub_str = []
    op = set()
    string = list(string)
    for _ in string:
        sub_str.append(string[:(length//num)])
        del string[:(length//num)]
    print("list :",sub_str)
    for i in sub_str:
        for j in i:
            op.add(j)
    print("set :",op)
    
merge(s,k)