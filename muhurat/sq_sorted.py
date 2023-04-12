def sortedSquares(nums):
    sq = []
    for i in range(len(nums)):
        c = nums[i] * nums[i]
        sq.append(c)

    def merge(sq,st1,ed1,st2,ed2):
        p1 = st1
        p2 = st2
        k = []
        while p1<=ed1 and p2<=ed2 :
            if sq[p1] < sq[p2] :
                k.append(sq[p1])
                p1 = p1 + 1

            else :
                k.append(sq[p2])
                p2 = p2 + 1

        while p1<=ed1:
            k.append(sq[p1])
            p1 = p1 + 1  

        while p2<=ed2:
            k.append(sq[p2])
            p2 = p2 + 1 

        id = 0
        while id < len(k) :
                sq[st1+id] = k[id]
                id = id + 1
            
        return sq    
           

    low = 0
    high = len(sq)-1
    def mergefuc(sq,low,high):
       
        mid = (low+high)//2
        if low == high:
            return 
        mergefuc(sq,low,mid)
        mergefuc(sq,mid+1,high)
        merge(sq,low,mid,mid+1,high)
    mergefuc(sq,0,len(sq)-1)


nums = [2,5,-1,-5,4]
re = sortedSquares(nums)
print(re)