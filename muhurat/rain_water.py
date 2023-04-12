class Solution:
    def trap(self, height):
        p1 = 0
        p2 = len(height)-1
        lmax = 0
        rmax = 0
        res = 0
        while p1 < p2:
            lmax = max(lmax, height[p1])
            rmax = max(rmax, height[p2])
            if height[p1] < height[p2]:
                res += lmax - height[p1]
                p1 = p1+1
            else:
                res += rmax - height[p2]
                p2 = p2-1
        return res