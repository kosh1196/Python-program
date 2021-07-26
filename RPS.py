import random

def get_random_choice():
    tools = ["Rock", "Paper", "Scissors"]
    return random.choice(tools)

computer_wins = 0
human_wins = 0

while True:
    computer_choice = get_random_choice()
    human_choice = raw_input("Please provide your input (Rock, Paper, Scissors): ")
   # human_choice = human_choice.title()

    if human_choice != "Rock" and human_choice != "Paper" and human_choice != "Scissors":
        print("Invalid input. Terminating")
        break

    if human_choice == computer_choice:
        print("Tie. I also chose ",computer_choice)
    elif human_choice == "Rock":
        if computer_choice == "Paper":
            print("I won: I chose ",computer_choice)
            computer_wins += 1
        elif computer_choice == "Scissors":
            print("You won: I chose ",computer_choice)
            human_wins += 1
    elif human_choice == "Paper":
        if computer_choice == "Rock":
            print("You won: I chose ",computer_choice)
            human_wins += 1
        elif computer_choice == "Scissors":
            print("I won: I chose ",computer_choice)
            computer_wins += 1
    elif human_choice == "Scissors":
        if computer_choice == "Rock":
            print("I won: I chose ",computer_choice)
            computer_wins += 1
        elif computer_choice == "Paper":
            print("You won: I chose %s.",computer_choice)
            human_wins += 1

    print("Score: Human",human_wins," vs Computer ", computer_wins)
    print()

if human_wins > computer_wins:
    print("Congrats! You won the game!")
elif computer_wins > human_wins:
    print("Sorry! I won the game!")
else:
    print("Tie! Let's do another one, if you are brave!")

