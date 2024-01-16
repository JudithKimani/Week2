#Rock paper scissors
import random

while True:
    user_action = input("Enter choice(rock, paper, scissrs): ")
    possible_actions = ["rock", "paper","scissors"]
    computer_action = random.choice (possible_actions)
    print(f"\nyou chose{user_action}, computer chose{computer_action}.\n")

    if user_action == computer_action:
        print("Both players selected {user_action}. Its a tie!")
    elif user_action =="rock":
        if computer_action == "scissors":
            print("Rock smashes the scissors!You win!")
        else:
            print("The paper cover the rock! You lose!")
    elif user_action =="paper":
        if computer_action == "scissors":
            print("Scissors cuts the paper!You lose!")
        else:
            print("The paper covers the rock!You win!")
    elif user_action =="scissors":
        if computer_action == "rock":
            print("The rock smashes the scissors!You lose!")
        else:
            print("The scissors cuts the paper!You win!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
            break
