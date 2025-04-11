# Lesson 4
import math

print("Enter fence sec 1 (use F for each plank):")
fenceOne = input()
print("Enter fence sec 2 (use F for each plank):")
fenceTwo = input()
print("Enter fence sec 3 (use F for each plank):")
fenceThree = input()

totalPlanks = len(fenceOne) + len(fenceTwo) + len(fenceThree)

dozen = 12
costPerDozen = 14.95

dozensNeeded = math.ceil(totalPlanks / dozen)
totalCans = dozensNeeded * dozen
leftoverCans = totalCans - totalPlanks
totalCost = dozensNeeded * costPerDozen

print(totalCans)
print(leftoverCans)
print(f"{totalCost:.2f}")
# End of Lesson 4