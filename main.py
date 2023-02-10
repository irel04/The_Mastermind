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
    while True:
        guess = input("Guess the color combination: ").upper().split(" ") # Split method allow us to separate the input and turn it into a list

        # Filtering the user input if he entered insufficient colors to the prompt
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        # Spectating if the color given by the user is valid or in the given list of color
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break
        
        return guess

# THis function is for checking and validating if the guess of the user is/has the same color combination with the color generator
def check_code(guess, key_to_correction):
    