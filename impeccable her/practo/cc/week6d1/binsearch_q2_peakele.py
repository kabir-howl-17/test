def findPeakElement( nums):
        
        l = 0
        h = len(nums) - 1
        
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                h = mid
        return l


nums = [1,2,1]
a = findPeakElement(nums)
print(a)
                