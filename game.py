import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guess the Number")
print("I'm thinking of a numberbetween 1and100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(" low ")
        elif guess > secret_number:
            print(" hight ")
        else:
            print(f"Correct! You got it in {attempts} attempts")
            break

    except ValueError:
        print("Please enter a valid number.")
