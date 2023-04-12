height = [4,2,0,3,2,5]
def trap(height):
    left = []
    right = []
    res = 0
    for i in range(len(height)):
        if i == 0:
            left.append(height[i])
        else:
            left.append(max(height[i],left[-1]))

    for i in range(len(height)-1,-1,-1):
        if i == len(height)-1:
            right.append(height[-1])
        else:
            right.append(max(right[-1],height[i]))
    right.reverse()
    for i in range(len(height)):
        res = res+ (min(left[i],right[i])-height[i])
    return res

print(trap(height))


'''class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        curr = 0
        water = 0
        while curr < len(height):
            while len(stack)!= 0 and height[curr]> height[stack[-1]]:
                top = height[stack.pop()]
                if len(stack)==0:
                    break
                d = curr - stack[-1]-1
                h = min(height[curr], height[stack[-1]]) - top
                water = water + d*h
            stack.append(curr)
            curr = curr + 1
        return water'''


    
        
