'''Q-1 ) Check if a number is Palindrome: (5 marks)
Given an integer, write a function that returns true if the given number is
palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
eg2:
Sample input:
1451
Sample output:
not palindrome.
'''


#iterative way 
n = int(input("enter the number to check= "))

'''st = str(n)
bst = st[::-1]
if st == bst:
    print(True)
else:
    print(False)'''


#recursive way

def palindrome(n,res):
    if n == 0:
        return res

    res = (res*10)+ (n%10)
    return palindrome(n//10, res) 

if __name__ == "__main__":
    n = int(input("enter the number to check= "))
    ans = palindrome(n,0)
    if ans == n:
        print(True)
    else:
        print(False)



