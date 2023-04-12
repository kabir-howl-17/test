'''Q-3) Find factorial of a number using recursion.
'''
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
    


if __name__ == "__main__":
    n = int(input("enter the number you want factorial of=  "))

    res = fact(n)
    print(res)