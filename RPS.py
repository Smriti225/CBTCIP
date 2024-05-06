import random

def play_game():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        return

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"Your choice: {user_choice}, Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Yeah !! You win")
    else:
        print("Oops !! You lose")


while True:
        play_game()
        play_again = input("Do you want to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


