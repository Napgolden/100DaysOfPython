import random

print("A Number Guessing Game!")
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100:\n"))
    if guess == secret_number:
        print("Congrats! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
