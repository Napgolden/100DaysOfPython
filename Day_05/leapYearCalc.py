#A program that calculates whether a year is a leap year
year = int(input("Enter a year to check whether it is a leap year:\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("It is a Leap Year")
else:
    print("Not a Leap Year")