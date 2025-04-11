# Lesson 23
total = 0
count = 0

while True:
    number = input("Enter a number or type done to finish: ")
    if number == "done":
        break
    if number.isdigit():
        total += int(number)
        count += 1

if count > 0:
    average = total / count
    print("The average is", average)
else:
    print("No valid numbers entered.")
# End of Lesson 23