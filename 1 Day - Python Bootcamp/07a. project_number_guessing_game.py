import random

target = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Guess the number between 1 and 100. You have 10 attempts!")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: "))
        attempts += 1

        if guess == target:
            print("🎉 You guessed it right!")
            break
        elif guess < target:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Please enter a valid integer.")

if guess != target:
    print("😢 You've exhausted all attempts. Better luck next time!")
    print("The correct number was:", target)

print("Your total attempts:", attempts)