import random


target = random.randint(1, 10)
attempts = 0
max_attempts = 2

while attempts < max_attempts:
    guess = int(input("Guess the number 1 - 10. You have 2 attempts! "))
    attempts += 1
    if guess == target:
        print("Success!")
        break
else:
    print("Sorry random number is ", target)