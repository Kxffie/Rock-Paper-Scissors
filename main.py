# Rock Paper Scissors in Python

from random import choice

choices = ["rock", "paper", "scissors"]

userChoice = input("Rock, Paper, or Scissors\n-> ")
userChoice = userChoice.lower()

computerChoice = choice(choices)

if userChoice == computerChoice:
    print("\nIt was a tie!\n")
elif userChoice == "rock":
    if computerChoice == "scissors":
        print("\nRock smashes scissors, you win!\n")
    else:
        print("\nPaper covers rock, you lose.\n")
elif userChoice == "paper":
    if computerChoice == "rock":
        print("\nPaper covers rock, you win!\n")
    else:
        print("\nScissors cuts paper, you lose.\n")
elif userChoice == "scissors":
    if computerChoice == "paper":
        print("\nScissors cuts paper, you win!\n")
    else:
        print("\nRock smashes scissors, you lose.\n")
elif userChoice not in choices:
    print("\nPlease choose Rock, Paper, or Scissors.\n")

input("Press enter to quit...")
