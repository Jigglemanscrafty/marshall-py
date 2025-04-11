# Lesson 5
print("Enter the amount of money you started with:")
startingMoney = float(input())
print("Enter cookie string (use 'b' for big and 'c' for normal cookies):")
cookieString = input()

normalCount = cookieString.count('c')
bigCount = cookieString.count('b')

normalSale = normalCount * 1.25
bigSale = bigCount * 2.00
totalSales = normalSale + bigSale

normalCost = normalCount * 0.50
bigCost = bigCount * 0.75
totalCost = normalCost + bigCost

profit = totalSales - totalCost
endingMoney = startingMoney + profit
totalCookies = normalCount + bigCount

print(totalCookies)
print(f"{profit:.2f}")
print(f"{endingMoney:.2f}")
# End of Lesson 5