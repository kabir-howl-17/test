nums = [1,2,2,2,3,7,7,6,1,1,3,4,4,3]

d = {}
for i in nums: # filling dictionary with frequancy of each number
    if d.get(i) is not None:
        d[i] += 1
    else:
        d[i] = 1
print(d)

def aainu(x): 
    return d[x]


bebu = sorted([k for k in d.keys()], reverse=True) 
        
inu = sorted(bebu, key = aainu)
#print(aainu)
print(inu)
print(bebu)

ans = []
for i in inu:
    for j in range(d[i]): 
        ans.append(i)
print(ans)