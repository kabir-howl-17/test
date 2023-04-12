nums = [1,3,5,6]
target = int(input("pick number= "))


def index(nums,target):
    l = 0
    h = len(nums)-1
    while l<=h:
        mid = (l+h)//2
        
        if nums[mid] == target :
            return mid
        
        elif nums[mid] > target :
            h = mid -1 

        else:
            l = mid +1
            res = l
            
    return res        


re = index(nums,target)
print(re)
