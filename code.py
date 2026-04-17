"""
The classes and methods that will be used to create this project are:

The Player class: Contains def move_player() and def get_energy()

The Wall class: def generate_wall(), def is_move_valid(), and def display_wall()

The Game class: def key_press(), def check_win(), def check_game_over(), def game_loop()


The functions that will be used to create this project are:

def move_player(): This function would allow the player to move around the rock climbing wall and on to the rock climbing holds if available.

def get_energy(): This function would be responsible for the energy that the player will recieve and the energy that the play might lose. It controls how the energy cahnges each move.

def generate_wall(): This function will be used tocreate the rock climbing wall and place all of the holds on to the rock climbing wall.

def display_wall(): This function will show the position of the character on the wall.

def key_press(): This function will process what keys need to be pressed in order to move the character.

def is_move_valid(): This function will check to see if the move being conducted is allowed in the context of the game.

def check_win(): This function will check to see if the play has reached the top and has won.

def check_game_over(): This function is the overall ending of the game if the charachter dies. This code will check to see if the player has run out of energy and, if so, the game is over.

def game_loop(): this function will control the entire game flow and call all of the function in the correct order.
"""


class Player:
    def __init__(self, start_row, start_column):
        self.row = start_row
        self.column = start_column
        self.energy = 10
    def move_player(self, direction):
        if direction == "w": #up
            self.row -= 1
        elif direction == "s": #down
            self.row += 1
        elif direction == "a": #left
            self.column -= 1
        elif direction == "d": #right
            self.column += 1
    def get_energy(self, resting):
        if resting:
            self.energy += 2 #gain energy
        else:
            self.energy -= 1 #lose energy

class Game:
    def __init__(self):
        self.wall = Wall()
        self.player = Player(0, 0)
    def key_press(self, key):
        if key in ["w", "a", "s", "d"]:
            self.player.move_player(key)
    def check_win(self):
        return self.player.row == self.wall.height - 1
    def check_game_over(self):
        return self.player.energy <= 0
    def game_loop(self):
        while True:
            self.wall.display_wall(self.player)
            key = input("Enter a move (w/a/s/d): ")
            self.key_press(key)
            if self.check_win():
                print("Congratualtions! You have reached the top of the wall! You win!")
                break
            if self.check_game_over():
                print("Game Over! You have run out of energy.")
                break
class Wall:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.holds = self.generate_wall()
    def generate_wall(self):
        holds = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if (i + j) % 3 == 0:
                    row.append(True)
                else:
                    row.append(False)
            holds.append(row)
        return holds
    def is_move_valid(self, player):
        if 0 <= player.row < self.height and 0 <= player.column < self.width:
            return self.holds[player.row][player.column]
        return False
    def display_wall(self, player):
        for i in range(self.height):
            row = ""
            for j in range(self.width):
                if player.row == i and player.column == j:
                    row += "P "
                elif self.holds[i][j]:
                    row += "H "
                else:
                    row += ". "
            print(row)

if __name__ == "__main__":
    game = Game()
    game.game_loop()
