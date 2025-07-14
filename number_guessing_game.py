import random

number = random.randint(1, 100)

guess = int(input("what's your guess? "))

if guess == number:
    print("Correct")
elif guess < number:
    print("Too low")
else: 
    print("Too high")

    