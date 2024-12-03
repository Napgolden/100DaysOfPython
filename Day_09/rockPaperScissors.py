import random

print("Rock, Paper, Scissors!!!")
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nEnter your choice (rock, paper, scissors):\n").lower()
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("\nDo you want to play again? (yes or no):\n").lower()
    if play_again != "yes":
        print("Thanks for playing, Goodbye!")
        break
