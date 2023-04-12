'''Q-2 ) Write a function that prints digits of a number from left to right , using
recursion:(5 marks)
Sample Input:
1234567
Sample output:
1
2
3
4
5
6
7
'''

#recursive way

def digiprint(n):
    if n == 0:
        return
    digiprint(n//10)
    print(n%10)

if __name__ == "__main__" :
    digiprint(1234567)

#explanation of above question for Inu mam

#line 20 
b = 1234
c = b//10
print(c)
#in the explanation above we are simply eliminating the last digit by floor division

#line 21
print(c%10)
#here we are getting the last number as remainder