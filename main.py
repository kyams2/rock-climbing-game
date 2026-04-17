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
                print("Congratulations! You have reached the top of the wall! You win!")
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

