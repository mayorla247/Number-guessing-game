import random

print("🎲 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Random number
secret_number = random.randint(1, 100)

while True:
    # User input
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.\n")

    elif guess > secret_number:
        print("Too high! Try again.\n")

    else:
        print(f"🎉 Congratulations! You guessed the number: {secret_number}")
        break
