#BMI Calculator
weight = int(input("What is your current weight in KG:\n"))
height = float(input("What is your current height in meters:\n"))
solve = weight / (height * height)
roundedSolve = round(solve)
print(f"Your BMI according to the inputs given is: {roundedSolve}.")