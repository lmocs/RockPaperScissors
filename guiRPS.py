from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")

intro = Label(root, text = "Welcome to Rock, Paper, Scissors! ")
intro.grid(row = 0, column = 0, columnspan = 3)

choice_list = ['r', 'p', 's']

# Declaring labels here so I can override/update them after each game
tie = Label(root)
win = Label(root)
lose = Label(root)

global times_won
times_won = 0

global times_played
times_played = 0

global times_lost
times_lost = 0

global player_score
player_score = 0

global bot_score
bot_score = 0



# Function for rock scenarios
def rock_logic():
    # This deletes the intro text when the game begins
    intro.grid_forget()

    global tie
    tie.grid_forget()

    global win
    win.grid_forget()

    global lose
    lose.grid_forget()

    # These are the rock variable scenarios
    global player_choice
    player_choice = "r"

    global bot_choice
    bot_choice = random.choice(choice_list)

    if player_choice == bot_choice:
        tie = Label(root, text = "Both chose rock, it's a tie!")
        tie.grid(row = 0, column = 0, columnspan = 3)

        global times_played
        times_played += 1

    elif player_choice != bot_choice and bot_choice == 's':
        win = Label(root, text = "Rock beats scissors, you win!")
        win.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_won
        times_won += 1

    elif player_choice != bot_choice and bot_choice == 'p':
        lose = Label(root, text = "Paper beats rock, you lose!")
        lose.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_lost
        times_lost += 1
        

    # This prints the score after each game
    player_score = Label(root, text = "Player: " + str(times_won))
    total_games = Label(root, text = "Games Played: " + str(times_played))
    bot_score = Label(root, text = "Bot: " + str(times_lost))

    player_score.grid(row = 2, column = 0)
    total_games.grid(row = 2, column = 1)
    bot_score.grid(row = 2, column = 2)


# Function for paper scenarios
def paper_logic():

    # This deletes the intro text when the game begins
    intro.grid_forget()

    global tie
    tie.grid_forget()

    global win
    win.grid_forget()

    global lose
    lose.grid_forget()

    # These are the paper variable scenarios
    global player_choice
    player_choice = "p"

    global bot_choice
    bot_choice = random.choice(choice_list)

    if player_choice == bot_choice:
        tie = Label(root, text = "Both chose paper, it's a tie!")
        tie.grid(row = 0, column = 0, columnspan = 3)

        global times_played
        times_played += 1

    elif player_choice != bot_choice and bot_choice == 'r':
        win = Label(root, text = "Paper beats rock, you win!")
        win.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_won
        times_won += 1

    elif player_choice != bot_choice and bot_choice == 's':
        lose = Label(root, text = "Scissors beats paper, you lose!")
        lose.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_lost
        times_lost += 1
        
    # This prints the score after each game
    player_score = Label(root, text = "Player: " + str(times_won))
    total_games = Label(root, text = "Games Played: " + str(times_played))
    bot_score = Label(root, text = "Bot: " + str(times_lost))

    player_score.grid(row = 2, column = 0)
    total_games.grid(row = 2, column = 1)
    bot_score.grid(row = 2, column = 2)



# Function for scissors scenarios
def scissors_logic():

    # This deletes the intro text when the game begins
    intro.grid_forget()

    global tie
    tie.grid_forget()

    global win
    win.grid_forget()

    global lose
    lose.grid_forget()

    # These are the paper variable scenarios
    global player_choice
    player_choice = "s"

    global bot_choice
    bot_choice = random.choice(choice_list)

    if player_choice == bot_choice:
        tie = Label(root, text = "Both chose scissors, it's a tie!")
        tie.grid(row = 0, column = 0, columnspan = 3)

        global times_played
        times_played += 1

    elif player_choice != bot_choice and bot_choice == 'p':
        win = Label(root, text = "Scissors beats paper, you win!")
        win.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_won
        times_won += 1

    elif player_choice != bot_choice and bot_choice == 'r':
        lose = Label(root, text = "Rock beats Scissors, you lose!")
        lose.grid(row = 0, column = 0, columnspan = 3)

        times_played += 1

        global times_lost
        times_lost += 1
        
    # This prints the score after each game
    player_score = Label(root, text = "Player: " + str(times_won))
    total_games = Label(root, text = "Games Played: " + str(times_played))
    bot_score = Label(root, text = "Bot: " + str(times_lost))

    player_score.grid(row = 2, column = 0)
    total_games.grid(row = 2, column = 1)
    bot_score.grid(row = 2, column = 2)



# RPS Buttons
rock_button = Button(root, text = "Rock", command = rock_logic)
rock_button.grid(row = 1, column = 0)

paper_button = Button(root, text = "Paper", command = paper_logic)
paper_button.grid(row = 1, column = 1)

scissors_button = Button(root, text = "Scissors", command = scissors_logic)
scissors_button.grid(row = 1, column = 2)

exit_button = Button(root, text = "Exit Game", command = root.quit)
exit_button.grid(row = 3, column = 1)


root.mainloop()