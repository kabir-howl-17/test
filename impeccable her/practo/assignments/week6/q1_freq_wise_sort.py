def frequencySort( nums):
        d = {}
        for i in nums: # filling dictionary with frequancy of each number
            if d.get(i) is not None:
                d[i] += 1
            else:
                d[i] = 1


        def aainu(x): # a key which we use to sort by frequancy of number
            return d[x]


        bebu = sorted([k for k in d.keys()], reverse=True) # reverse the array because numbers with same frequancy must
         #be sorted in decreasing order
        inu = sorted(bebu, key=aainu) # now just sort by frequancy of every number
        ans = []
        for i in inu:
            for j in range(d[i]): 
                ans.append(i)  # filling array 'ans' of each number N times, where N - inu number of all number i in array inu.
        return ans


nums = [1,1,2,2,2,3]
res = frequencySort(nums)
print(res)