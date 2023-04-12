nums = [2,3,4,5,6]

target = 11
for i in range(len(nums)) : 
            first = nums[i]
            if (target - first) in nums[i+1:] : 
                print([i, nums[i+1:].index(target-first)+i+1])




