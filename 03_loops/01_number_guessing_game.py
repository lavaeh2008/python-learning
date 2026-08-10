# While Loops
# Number Guessing Game

secret_number = 7
guess = int(input("Guess a number: "))
attempts = 0

while guess != secret_number:
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")

    guess = int(input("Try again: "))
    attempts += 1

print("You guessed it!")
print("It took you", attempts, "attempts.")