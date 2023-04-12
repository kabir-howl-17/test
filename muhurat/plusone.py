'''You are given a large integer represented as an integer array digits,
 where each digits[i] is the ith digit of the integer. 
 The digits are ordered from most significant to least significant in left-to-right order.
  The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.'''



a = [1,2,3] #length
# out = [1,2,4]
l = len(a)
count = 1 
sums = 0
for i in range(l-1, -1,-1):
    sums = sums+a[i]*count
    count = count*10

dums = str(sums+1)
pums = []
for i in range(len(dums)):
    pums.append(int(dums[i]))
print(pums)


    


    



                            #1234 unit = 4, tens = 3*10, hund= 2*10*10, thous = 1*10*100