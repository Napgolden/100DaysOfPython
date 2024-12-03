print("Welcome to the Temperature Converter!")

print("\nChoose an option:")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2):\n")

if choice == "1":
    celsius = float(input("Enter the temperature in Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit:\n"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid choice. Please pick either 1 or 2.")
