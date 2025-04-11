# Lesson 9
import random

options = {"rock", "paper", "scissors"}

print("Choose rock, paper, or scissors:")
playerChoice = input().strip().lower()

while playerChoice not in options:
    print("Invalid input. Choose rock, paper, or scissors:")
    playerChoice = input().strip().lower()

cpuChoice = random.choice(list(options))

print(f"AI chose: {cpuChoice}")

if playerChoice == cpuChoice:
    print("It's a tie!")
elif playerChoice == "rock" and cpuChoice == "scissors":
    print("You win!")
elif playerChoice == "scissors" and cpuChoice == "paper":
    print("You win!")
elif playerChoice == "paper" and cpuChoice == "rock":
    print("You win!")
else:
    print("AI wins!")
# End of Lesson 9