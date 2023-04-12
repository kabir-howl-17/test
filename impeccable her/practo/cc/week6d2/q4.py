'''Q-4 ) [Bonus Question] Recursive implementation of binary search:
(5 extra marks)
We have seen an iterative approach for binary search algorithm , write a
recursive approach for that.
HINT: when we divide the array into two parts, we need to perform a search on only one half.'''

def bs(array, l, h, target):
    if l <= h:
        mid = (l+h)//2
        if array[mid] < target:
            return bs(array, mid+1, h, target)
        elif array[mid] > target:
            return bs(array, l, mid-1, target)
        else:
            return mid 
    else:
        return -1






if __name__ == "__main__":
    array = (12, 13, 15, 18, 19, 45, 45, 56, 58, 67, 89, 192, 201, 201, 341, 456)
    target = int(input("enter target here = "))

    res = bs(array, 0, len(array)-1, target)
    print(res)