from random import randint
tries = 1
result = randint(1,100)

guess = int(input("guess a number between 1-100 bud! = "))

while guess != result :
    if guess > result:
        print("GHANO BADO ")
        guess = int(input("guess again = "))
        tries = tries+1
    elif guess < result:
        print("GHANO CHOTO")
        guess = int(input("try again = "))
        tries = tries+1
print("congo! you got the number this time")
print("it took you", tries,"to guess the number")