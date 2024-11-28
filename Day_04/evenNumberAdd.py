#A program that adds all even numbers in a given number
targetNum = int(input("Enter the number:\n"))

totalEven = 0
for number in range(2, targetNum + 1, 2):
    totalEven = totalEven + number
print(totalEven)