
'''def twoSum(nums, target):
    inumam = {}
    ed = 0
    while ed < len(nums):
        if target-nums[ed] in inumam:
            arna = inumam[target-nums[ed]]
            return [arna,ed]
            ed = ed+1
            
        else:
            inumam[nums[ed]]= ed
            ed = ed+1'''
nums = [2,7,11,15]
target = 9
ina = {}
for i in range(len(nums)):
    ina[nums[i]] = i

    if target- nums[i] in ina:
        arna = ina[target-nums[i]]
        reco = i
print([arna,reco])
        
            
        

nums = [2,7,11,15]
target = 9
#print(twoSum(nums,target))