while True:
    user_input = input("Enter Mathematical Expression or Press 'q' to quit:\n")
    if user_input.lower() == "q":
        print("Goodbye!!")
        break
    try:
        result = eval(user_input)
        print(f"The result is {result}.")
    except:
        print("Invalid Input, Try Again")