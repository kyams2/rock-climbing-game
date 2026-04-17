# Description of Project

The overall idea of the project is that there is a rock climbing wall with many rock climbing holds. There is a character in the simulation     that a player controls. The player's objective is to get the character from the bottom of a rock climbing wall to the top of the rock           climbing wall. They use the computer keys to move the character up, but as the character continues to move, it loses energy, so the player      has to find rests in the game for the character to regenerate its power. If the character loses all of its energy before it reaches the top,    the game is over.

# Program Use
   
This program would generally be used for fun! By taking a character and being able to move it left, right, up, and down for a possibility of    winning, the player can create a fun time on their own or with friends. It is an easy way to pass the time quickly without the effort of doing a task with much work.

# Specific Outline of Code

## The classes and methods that will be used to create this project are:

The Player class: Contains def move_player() and def get_energy()

The Wall class: def generate_wall(), def is_move_valid(), and def display_wall()

The Game class: def key_press(), def check_win(), def check_game_over(), def game_loop()


## The functions (and descriptions) that will be used to create this project are:

def move_player(): This function would allow the player to move around the rock climbing wall and on to the rock climbing holds if available.

def get_energy(): This function would be responsible for the energy that the player will recieve and the energy that the play might lose. It controls how the energy cahnges each move.

def generate_wall(): This function will be used tocreate the rock climbing wall and place all of the holds on to the rock climbing wall.

def display_wall(): This function will show the position of the character on the wall.

def key_press(): This function will process what keys need to be pressed in order to move the character.

def is_move_valid(): This function will check to see if the move being conducted is allowed in the context of the game.

def check_win(): This function will check to see if the play has reached the top and has won.

def check_game_over(): This function is the overall ending of the game if the charachter dies. This code will check to see if the player has run out of energy and, if so, the game is over.

def game_loop(): this function will control the entire game flow and call all of the function in the correct order.


# Controls

The "w" key moves the character up the wall.
The "s" key moves the character down the wall.
The "a" key moves the character to the left.
The "d" key moves the character to the right. 

# Notes

This game does not take any inputted data, other than pressing keys to move the character. The code would take into account which keys would correlate to moving the character left, right, up, and down but there is no types data fromt he player.



