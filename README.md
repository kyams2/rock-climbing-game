# What is Rock Climbing?

Rock climbing is a physically intensive sport that requires mental and physical stamina. The goal is to attempt moves in order to get from the bottom of the rock wall to the top. In competing, the goal is to do this with the least amount of attempts. The strategic methods of finding rest holds to regain energy and conserve it, is crucial to get to the top of the wall.

# Demo (kya_project.py)
When the code is run:

+ A grid like wall appears which is the area that the character will be climbing on.

+ You control the character by using the keys "w", "a", "s", "d" to move it up, left, down, and right.

+ As you move the character around the wall, it collects energy by resting and loses energy by moving.

+ You should strategically maneuver around the wall to avoid losing all of the energy.

+ The overall objective is to get to the top of the rock climbing wall before the character's energy has run out.

# Context and Inspiration

I have been a competitive rock climber for almost ten years so this project was inspired by my passion for climbing. In rock climbing, the goal is to get to the top of the wall with the least amount of tries/falls as possible. Although a competitive climber, my project is based on the ideals of outdoor climbing on high mountains. Each section of a tall climb is called a "pitch", so each level would equate to a particular pitch of the climb. As the climb gets higher, the pitches might get harder. It is crucial to find resting positions on the wall to conserve and maximize your energy to make it to the top. Finding the most strategic and energy conserving way to get to the top, without knowing exactly which holds are the best to rest on, is another very important skill to master for success.

# Testing/Code Running

(This game is run in the terminal so no installation, other than python, is needed. If on Windows, install the curses package that is not currently installed using this in the terminal: pip install windows-curses)

1) Navigate to the kya_project.py page in my github repository.

2) In the upper right-hand corner of the page, download the raw file of the code.

3) This should automatically place the file into your Downloads section on MAC or a similar section on PC.

4) Open your terminal on the computer you are using and navigate to the location that the file downloaded to using a series of cd commands and then run the page using the uv run python command. EX. cd Downloads/uv run python kya_project.py

* When running the game, the character, P, should be at the bottom left hand of the grid. It should move up and down depending on which key is pressed ("w" "a" "s" "d"). As the character makes a move, the energy will go down depending on what hold you move to. Once the character gets to the top, a new level will generate. After 10 levels are completed, you have won/reached the top of the mountain, but if the character loses all of its energy before it reaches the top, the game is over.

# Controls

The "w" key moves the character up the wall.

The "s" key moves the character down the wall.

The "a" key moves the character to the left.

The "d" key moves the character to the right. 

# UNIT TEST 1 NARRATIVE OF CURRENT CODE (NO INPUT DATA)

Currently, have completed the coding for the first class out of three. This is the Player class.
This class has two functions with it (excluding def __init__):

The def move_player function has set each key in "w, a, s, d" to a specific direction that the character would be moving in. 
"w" makes the character move up, "s" is down, "a" is left, and "d" is right. After defining the letter to the general direction, it is crucial to assign which specific direction it will me moving. Underneath each "if" or "elif" statement, this is where I assigned each specific direction with "self.row" or "self.column" and it should check out.

The get_energy function is coded for the character to receive or lose energy. "if" the character is resting/stopped, 
it will gain two energy points but if the character is moving/not resting, the character will lose one energy point.

# UNIT TEST 2 NARRATIVE OF CURRENT CODE

In this stage of the project, I have completed most of the code. When run, the code outputted something very similar to my overall end goal of the project. When I push the "w", "a", "s", "d" keys, the character moves up and down the wall like it is supposed to. The wall is also generated with all of the holds in a grid like pattern, and the congratulatory words are printed when the player wins at the end of the game. There are a few problems that I am currently working on: The entire wall prints in the terminal again every time the player makes the character move, the player actually moves down the wall instead of up the wall and finished at the bottom, and the obstacles, such as the loss of points, seem to not be an issue when playing the game which makes it way too easy to accomplish the goal.

# UNIT TEST 3 NARRATIVE OF CURRENT CODE

In this stage of the project, I have completed my entire code and have a running and working game. The game is continuing as expected and there are no huge errors preventing it from happening. I have fixed the wall problem in the sense that the wall does not print every time the player wants to move the character, it just prints once and then stays on the screen until the player loses. I have fixed the issue of the player moving down on the grid in the terminal and now the player moves the character up. I have also made the game a bit more competitive in the sense that the player actually has to strategically use their rests to get to the top and not run out of energy too quickly. The final thing that I have to fix is that, when run, the game automatically quits after level four due to the increase in holds on the wall so I have to fix that in order for my game to run properly.

# Extras!

## Specific Outline of Code

### The classes and methods/functions that will be used to create this project are:

The Player class: def __init__, def move_player(), def get_energy()

The Game class: def __init__, def next_level, def key_press(), def check_win(), def check_game_over(), def game_loop()

The Wall class: def __init__, def generate_wall(), def is_move_valid(), def display_wall()


### The functions (and descriptions) that will be used to create this project are:

def move_player(): This function allows the player to move around the rock climbing wall and on to the rock climbing holds if available.

def get_energy(): This function is responsible for the energy that the player will recieve and the energy that the play might lose. It controls how the energy changes each move.

def next_level(): This function is responsible for generating the next level of the game if the player has won the previous level.

def generate_wall(): This function is responsible for creating the rock climbing wall and place all of the holds on to the rock climbing wall.

def display_wall(): This function shows the position of the character on the wall.

def key_press(): This function processes what keys need to be pressed in order to move the character.

def is_move_valid(): This function checks to see if the move being conducted is allowed in the context of the game.

def check_win(): This function checks to see if the play has reached the top and has won.

def check_game_over(): This function is the overall ending of the game if the character dies. This code will check to see if the player has run out of energy and, if so, the game is over.

def game_loop(): This function controls the entire game flow and call all of the function in the correct order.

## Program Use
   
This program would generally be used for fun! By taking a character and being able to move it left, right, up, and down for a possibility of winning, the player can create a fun time on their own or with friends. It is an easy way to pass the time quickly without much effort. It will give a bit of insight into the rock climbing world and introduce the basic concepts of this sport.

## Notes

This game does not take any inputted data, other than pressing keys to move the character. The code would take into account which keys would correlate to moving the character left, right, up, and down but there is no typed data from the player.



