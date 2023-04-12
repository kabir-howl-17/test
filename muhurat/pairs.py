'''Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.'''

nums = ["a", "b", "c","a", "a", "c"]
pair = 0 
end = 0
hashtable = {}

while end < len(nums):
    if nums[end] not in hashtable:
        hashtable[nums[end]]= 1
        end = end +1
    else:
        pair = pair + hashtable[nums[end]]
        hashtable[nums[end]] = hashtable[nums[end]]+1
        end =  end+1
    print(hashtable)
    print(pair)


