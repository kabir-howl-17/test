
def sortedSquares(nums):
    sq = []
    for i in range(len(nums)):
        c = nums[i] * nums[i]
        sq.append(c)









def merged(bebu, lf,ll, rf,rl):
    p1 = lf
    p2 = rf
    inu_mam = [ ]

    while p1<=ll and p2<=rl:
        if bebu[p1]<bebu[p2]:
            inu_mam.append(bebu[p1])
            p1 += 1
        else:
            inu_mam.append(bebu[p2])
            p2 += 1
    
    while p1<=ll:
        inu_mam.append(bebu[p1])
        p1 += 1

    while p2<= rl:
        inu_mam.append(bebu[p2])
        p2 += 1

    cutu = 0
    while cutu< len(inu_mam):
        bebu[lf+cutu] = inu_mam[cutu]
        cutu += 1
    return bebu


def mergesort(bebu, l, h):
    mid = (l+h)//2
    if l == h:
        return
    
    mergesort(bebu,l,mid)
    mergesort(bebu,mid+1, h)
    merged(bebu,l,mid,mid+1,h)



if __name__ == "__main__":

    bebu = [23,45,67,45,23,54,12,56,78,4,5,2]

    mergesort(bebu,0, len(bebu)-1)
    #print(bebu)



    