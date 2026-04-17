# UNIT TEST 1 NARRATIVE OF CURRENT CODE (NO INPUT DATA)

Currently, have completed the coding for the first class out of three. This is the Player class.
This class has two functions with it (excluding def __init__):

The def move_player function has set each key in "w, a, s, d" to a specific direction that the character would be moving in. 
"w" makes the character move up, "s" is down, "a" is left, and "d" is right. After defining the letter to the general direction, 
it is crucial to assign which specific direction it will me moving. Underneath each "if" or "elif" statement, this is where I 
assigned each specific direction with "self.row" or "self.column" and it should check out.

The get_energy function is coded for the character to receive or lose energy. "if" the character is resting/stopped, 
it will gain two energy points but if the character is moving/not resting, the character will lose one energy point.

# UNIT TEST 2 NARRATIVE AND CODE RUN

In this stage of the project, I have completed most of the code. When run, the code outputted something very similar to my overall end goal of the project. When I push the "w", "a", "s", "d" keys, the character moves up and down the wall like it is supposed to. There are a few problems that I am currently working on: The entire wall prints in the terminal again every time the player makes the character move, the player actually moves down the wall instead of up the wall and finished at the bottom, and the obstacles, such as the loss of points, seem to not be an issue when playing the game. The code of the current project is printed:

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
