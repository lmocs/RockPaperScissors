import random

print("Welcome to Rock, Paper, Scissors!")

player_choice = input("Please choose r, p, or s: ")
opt = "rps"
bot_choice = (random.choice(opt))

def game():
    if player_choice == "r" and bot_choice == "p":
        return "Paper beats rock! You lost!"

    elif player_choice == "s" and bot_choice == "r":
        return "Rock beats scissors! You lost!" 

    elif player_choice == "p" and bot_choice == "s":
        return "Scissors beats paper! You lost!"

    elif player_choice == "r" and bot_choice == "s":
        return "Rock beats scissors! You won!"

    elif player_choice == "s" and bot_choice == "p":
        return "Scissors beats paper! You won!"

    elif player_choice == "p" and bot_choice == "r":
        return "Paper beats rock! You won!"

    elif player_choice == bot_choice:
        return "It's a tie! Play again!"

    else:
        return "Restart game!"

print(game())