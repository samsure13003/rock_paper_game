import random


def get_valid_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")


def play_game():
    rounds = 3
    choices = ["rock", "paper", "scissors"]

    for _ in range(rounds):
        user_choice = get_valid_choice()
        computer_choice = random.choice(choices)

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")


def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break


main()
