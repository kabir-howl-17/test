#make aainu solve it tooo

def findMedianSortedArrays( nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        p1 = 0
        p2 = 0
        c = []
        while p1<m and p2<n:
            if nums1[p1]<nums2[p2]:
                c.append(nums1[p1])
                p1 = p1+1
            else:
                c.append(nums2[p2])
                p2 =  p2+1
        while p1<m:
            c.append(nums1[p1])
            p1 = p1+1

        while p2<n:
            c.append(nums2[p2])
            p2 =  p2+1
        print(c)
        mid = len(c)//2
        print(mid)
        if len(c)%2 == 0:
            blue = (c[mid]+c[mid-1])/2
            return blue
        else:
            return c[mid]
nums1 = [1,3]
nums2 = [2]

re = findMedianSortedArrays(nums1, nums2)
print(re)