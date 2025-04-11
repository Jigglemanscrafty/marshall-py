# Lesson 8
winCount = 0

for i in range(6):
    print(f"Enter result for game {i + 1} (W or L):")
    result = input().strip().upper()
    if result == 'W':
        winCount += 1

if winCount >= 5:
    print("Group 1")
elif winCount >= 3:
    print("Group 2")
elif winCount >= 1:
    print("Group 3")
else:
    print("Disqualified")
# End of Lesson 8