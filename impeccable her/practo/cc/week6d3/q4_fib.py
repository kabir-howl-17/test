'''Q-4) Find nth number in fibonacci series using recursion'''



def fib(n):
    if n ==0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)





if __name__ == "__main__":
    n = int(input("enter number here = "))

    res = fib(n)
    print(res)