import random

target = random.randint(1, 100)
attempts = 0

print("Guess a number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == target:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
        break
    elif guess < target:
        print("Too low!")
    else:
        print("Too high!")
