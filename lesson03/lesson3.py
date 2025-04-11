# Lesson 3
import math

userNumber = int(input("Enter number of tiles you have: "))
if userNumber <=0:
    print("You must enter a whole, positive number.")
else:
    root = (math.sqrt(userNumber))
    if root == int(root):
        print("The max number of tiles for each side is", int(root))
    else: 
        print("The max number of tiles for each side is", math.floor(root))
# End of lesson 3