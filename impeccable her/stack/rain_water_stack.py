height = [4,2,0,3,2,5]

def trap(height):
    queue = list()
    p = 0
    water = 0
    l = len(height)

    while p <  l:

        while len(queue) != 0 and height[p] > height[queue[0]]:
           
           top = height[queue.pop(0)]
           if len(queue) == 0:
              break
           d = p - queue[0]+1
           h = min(height[p],height[queue[0]])-top
           water = water+ d*h
        queue.append(p)
        p = p+1
    return water  
print(trap(height))
