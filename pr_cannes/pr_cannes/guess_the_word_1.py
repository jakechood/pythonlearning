'''A board is an int matrix framed with strs _ and |. 
For example, the board
    ________________
    |              |
    |              |
    |              |
    |              |
    |              |
    |              |
    |              |
    |              |
    |              |
    |              |
    |______________|
is drawn using the turtle function


A completed board is a board with the goal image.
For example, the board 
    ________________
    |        |\    |
    |        | \   |
    |  ______|  \  |
    | /   \      | |
    ||__/        | |
    | \____      | |
    |      |     | |
    |      |     | |
    |      |     | |
    |      |     | |
    |______|_____|_|
is a completed board for the goalword "Llama"
completed by the turtle function
 '''


import turtle_frame
'''Prep window for interaction'''
import tkinter as tk

'''Tell the user what's going on'''
import turtle_frame 
greeting = tk.Label(text="Welcome to Guess The Word!")


game_instr1 = tk.Label(text="This is the frame for an image.")
game_instr2 = tk.Label(text="Each time you guess a letter correctly, the cursor will move.")
game_instr3 = tk.Label(text="If you guess incorrectly, you will receive an error message.")
game_instr4 = tk.Label(text="The goal is to guess the word matching the image.")
game_instr5 = tk.Label(text="To exit the game, enter the number '0'")
game_instr6 = tk.Label(text="The game has begun")
input("Guess the letter:")

greeting.pack()
game_instr1.pack()
game_instr2.pack()
game_instr3.pack()
game_instr4.pack()
game_instr5.pack()
game_instr6.pack()

guess_count = int(0)

if input():
    guess_count += 1

'''Final correct answer'''
import pr_cannes.full_llama as full_llama

congrats = tk.Label(text="Congratulations! You won!")
guesses = tk.Label(text = "Guesses: " + guess_count)
congrats.pack()
guesses.pack()