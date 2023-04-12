def mergef(inu, sl,el,rl,er):
    p1 = sl
    p2 = rl
    c = []

    while p1 <= el and p2 <= er:
        if inu[p1]< inu[p2]:
            c.append(inu[p1])
            p1 = p1 + 1
        else:
            c.append(inu[p2])
            p2 = p2 + 1
    
    while p1 <= el:
        c.append(inu[p1])
        p1 = p1+1
        
    while p2 <= er:
        c.append(inu[p2])
        p2 = p2 + 1


    idx = 0
    while idx < len(c):
        inu[idx] = c[idx]
        idx = idx+1
    return inu



if __name__ == "__main__":
    inu = [1,3,5,7,2,4,6,8]
    bebu = mergef(inu, 0, 3, 4, 7)
    print(bebu)
    


    
