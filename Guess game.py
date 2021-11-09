import random
n = random.randint(0,20)
chance=3

while "guess" != n:
    guess = int(input("Enter the guess number:"))

    if guess < n:
        print("Too low")
        chance = chance - 1
    elif guess > n:
        print("Too high")
        chance = chance - 1
    else:
        print("Correct")
        break

    if chance==0:
        print("Chances over!!! Please try again!!!")
        break


