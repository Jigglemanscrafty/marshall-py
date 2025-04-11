# Lesson 7
import random

print("Enter the difficulty class (DC) to beat:")
difficultyClass = int(input())

diceRoll = random.randrange(1, 21)

print(f"You rolled: {diceRoll}")

if diceRoll >= difficultyClass:
    print("Success!")
else:
    print("Fail!")
# End of Lesson 7