import random

number = random.randint(1, 100)



while True:
    try:
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

    