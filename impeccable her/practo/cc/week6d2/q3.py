'''Q-3 ) Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
'''

#recursive way

def recrevst(st):
    if len(st) == 0:
        return
    
    huh = st[0]
    recrevst(st[1:])
    print(huh)


if __name__ == "__main__" :
    recrevst("aainasharma")