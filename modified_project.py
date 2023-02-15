import random
from Binary_Tree_Class import *

# Defining our list of colors for the game
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 2
CODE_LENGTH = 4

def build_tree(colors):
    root = BinarySearchTreeNode(colors[0])

    for i in range(1, len(colors)):
        root.add_child(colors[i])

    return root

def bubble_sort(color_pick):
    for i in range(len(color_pick)-1, 0, -1):
        for j in range(i):
            if color_pick[j] > color_pick[j+1]:
                temp = color_pick[j]
                color_pick[j] = color_pick[j+1]
                color_pick[j+1] = temp

# Creating our function for creating 4-color combination from the COLORS list
def generate_code():
    code = []


    for i in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    # Using the bubble so that the combination will be arrange further
    bubble_sort(code)

    return code

# This function will allow us to get input from the users
def player_guess(value):
    while True:
        guess = value.upper().split(" ") # Split method allow us to separate the input and turn it into a list

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
def check_code(guess, key_to_correction, bi_tree):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    # Iterating the color in the key then making if-else statement to check then append it to dictionary
    for color in key_to_correction:
        if bi_tree.search(color):
            if color in color_count:
                pass
            else:
                color_count[color] = 0
        color_count[color] += 1
    
    # Comparing which colors are in correct position
    for guess_color, real_color in zip(guess, key_to_correction):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1
    
    # Checking if the guess color is in the list of the correct answer and not reusing the one who has partnered color
    for guess_color, real_color in zip(guess, key_to_correction):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1
    
    return correct_pos, incorrect_pos

# We'll make a function for executing the game
code = generate_code()
color_count_tree = build_tree(code)

def game(value):
    
    for attempts in range(1, TRIES + 1):
        
        guess = player_guess(value)
        correct_pos, incorrect_pos = check_code(guess, code, color_count_tree)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        return f"Correct position/s: {correct_pos} | Incorrect position/s: {incorrect_pos}"

    else:  
        return "You ran out of tries, the code was: ", *code


