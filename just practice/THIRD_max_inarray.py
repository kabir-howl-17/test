'''Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

 '''


nums = [1,3,5,5,6,7,8,9,10,9,8,8,9,5]


rain = list(set(nums))
print(rain)
aainu= sorted(rain, reverse = True)
if len(aainu)<3:
    print(aainu[0])
else:
    print(aainu[2])