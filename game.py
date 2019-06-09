import random

options = ["rock", "paper", "scissors"]
'''
def determine_winner(user_input, computer_input):
    if user_input == "rock":
        if computer_input == "rock":
            print("The game is tied! Play again")
        elif computer_input == "paper":
            print("You lost. The computer won the game")
        else:
            print("Congratulations!! You won")
    elif user_input == "paper":
        if computer_input == "paper":
            print("The game is tied! Play again")
        elif computer_input == "scissors":
            print("You lost. The computer won the game")
        else:
            print("Congratulations!! You won")
    else:
        if computer_input == "scissors":
            print("The game is tied! Play again")
        elif computer_input == "rock":
            print("You lost. The computer won the game")
        else:
            print("Congratulations!! You won")
    return
'''

def determine_winner(UI, CI):
    if UI == "rock":
        if CI == "rock":
            winner = None
        elif CI == "paper":
            winner = "paper"
        else:
            winner = "rock"
    elif UI == "paper":
        if CI == "paper":
            winner = None
        elif CI == "rock":
            winner = "paper"
        else:
            winner = "scissors"
    else:
        if CI == "scissors":
            winner = None
        elif CI == "rock":
            winner = "rock"
        else:
            winner = "scissors"
    return winner

# only if this script is executed in command line
if __name__ == "__main__":

    # This code enables the game of rock - paper - scissors.
    print("Welcome to the game of rock-paper-scissors. Follow the instructions and enjoy the game. May the best man win")

    # USER INPUT
    user_choice = input("Select Rock, Paper or Scissors. You can make only one choice.").lower()

    print("The user has selected {}".format(user_choice))

    # USER INPUT VALIDATION
    if user_choice not in options:
        print("You made an invalid choice. Please start again and select between rock, paper or scissors. You can only make one choice.")
        exit()
    else:
        pass

    # COMPUTER INPUT
    computer_choice = random.choice(options).lower()
    print("The computer has chosen {}".format(computer_choice))


    # USER INPUT VS COMPUTER INPUT LOGIC 

    winning_choice = determine_winner(user_choice, computer_choice)
    breakpoint()
    if winning_choice:
        if winning_choice == user_choice:
            print("Congratulations!! You have won")
        else:
            print("Oh No, the computer has won")
    else:
        print("It is a tie!!")

    print("Thank you, Comeback!!")