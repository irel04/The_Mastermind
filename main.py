import random

# Defining our list of colors for the game
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# Creating our function for creating 4-color combination from the COLORS list
def generate_code():
    code = []

    for i in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

# This function will allow us to get input from the users
def player_guess():
    guess = input("Guess the color combination: ").upper().split(" ") # Split method allow us to separate the input and turn it into a list
    

