# Lesson 12
print("Enter angle 1:")
angleOne = int(input())

print("Enter angle 2:")
angleTwo = int(input())

print("Enter angle 3:")
angleThree = int(input())

total = angleOne + angleTwo + angleThree

if total == 180:
    if angleOne == angleTwo == angleThree:
        print("Equilateral")
    elif angleOne == angleTwo or angleOne == angleThree or angleTwo == angleThree:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle.")
# End of Lesson 12