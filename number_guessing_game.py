import random

number = random.randint(1, 100)

max_attempts = 10
attempt = 0

while attempt < max_attempts:
    try:
        attempt += 1
        guess = int(input("what's your guess? "))

        if guess == number:
            print("Correct")
            break
        elif guess < number:
             print("Too low")
        else: 
            print("Too high")
    except ValueError:
        print("Please enter a valid integer.")

if attempt == max_attempts:
    print(f"You've used all your attempts. The number was {number}.")