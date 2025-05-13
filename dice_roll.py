import random

def roll_dice():
    return random.randint(1, 6)

while True:
    a = input("Press Enter to roll the dice or type 'q' to quit: ")
    if a.lower() == 'q':
      print("Goodbye!")
      break
    else:
     result = roll_dice()
     print(f"You rolled a {result}")