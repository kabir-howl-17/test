stupid = "solidstupid"


def solid(sub):
    for i in range(len(sub)):
        if sub[i] in sub[:i]+sub[i+1:]:
            return False
    return True


def darling(stupid):
    for i in range(len(stupid)):
        for j in range(i,len(stupid)):
            sub = stupid[i:j+1]
            #print(sub)

            if not solid(sub):
                maxi =  0
                maxi = max(maxi,len(sub))
    return maxi


pro = darling(stupid)
print(pro)