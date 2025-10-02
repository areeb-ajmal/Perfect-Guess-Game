import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n :
    guesses += 1
    a = int(input("Enter your Number : "))

    if a > n :
        print("Enter Lower number please!")

    else :
        print("Enter Higher number please!")

print(f"Congratulations you have guessed {n} in {guesses} attepmts")




