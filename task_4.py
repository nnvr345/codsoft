import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def display_choices(user_choice, computer_choice):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    print("ROCK, PAPER, SCISSORS GAME")

    while True:
        print("\nChoose: rock, paper, scissors, or quit")
        user_choice = input("Your choice: ").lower()

        if user_choice == "quit":
            print("Quitting the game. Goodbye!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, scissors, or quit.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        display_choices(user_choice, computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Quitting the game. Goodbye!")
            break

if __name__ == "__main__":
    rock_paper_scissors()
