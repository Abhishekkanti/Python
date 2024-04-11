


def swap_case(s):
    op =[]
    for i in s:
        if s[0].islower():
            op.append(i.upper())
        elif i.upper():
            op.append(i.lower())
    for j in op:
        x = "".join(op)
    return x

s = input()
result = swap_case(s)
print (result)

        