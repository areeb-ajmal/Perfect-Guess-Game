import random

n = random.randint(1, 100)
a = -1
guesses = 1

while a != n :
    a = int(input("Enter your Number : "))

    if a > n :
        print("Enter Lower number please!")
        guesses += 1

    elif (a < n):
        print("Enter Higher number please!")
        guesses += 1

print(f"Congratulations you have guessed {n} in {guesses} attepmts")





