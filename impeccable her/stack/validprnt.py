def validparen(st):
    ob = 0
    cb = 0
    for i in st:
        if i == "(":
            ob = ob +1
        elif i == ")":
            cb = cb+1
        if ob>= cb:
            continue
        else:
            return "invalid"
    if ob == cb :
        return "valid"
    return "invalid out"

st = "((()))("
print(validparen(st))
