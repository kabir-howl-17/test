nums = [10,20,30,5,10,50]

def max_asce(nums):
    p1 = 0
    p2 = 1
    maxi = nums[p1]
    movi = nums[p1]
    while p2<len(nums):
        if nums[p2]>nums[p1]:
            movi = movi+nums[p2]
            maxi = max(movi,maxi)
            p2 = p2+1
            p1 = p1+1
        else:
            p1 = p2
            p2 = p2+1
            movi = nums[p1]
    return maxi

re = max_asce(nums)
print(re)

