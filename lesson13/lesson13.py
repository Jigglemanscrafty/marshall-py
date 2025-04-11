# Lesson 13
month = int(input("Enter month, in numerical value (ex: January = 1): "))
day = int(input("Enter day of the month (ex: 1, 2, 3): "))
if 12 >= month >= 1 and 31 >= day >= 1:
    if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31 or month in [4, 6, 9, 11] and day <= 30 or month == 2 and day <= 29 and month and day >= 1:
        if month > 2:
            print("After.")
        elif month < 2:
            print("Before.")
        else:
            if day > 18:
                print("After.")
            elif day < 18:
                print("Before.")
            else:
                print("Special.")
    else:
        print("Invalid date.")
else:
    print("Invalid date.")
# End of Lesson 13