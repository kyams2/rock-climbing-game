import random
import curses

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
        self.player = Player(self.wall.height - 1, 0)
        self.wall.holds[self.wall.height - 1][0] = True
        self.message = ""
    def key_press(self, key):
        if key in ["w", "a", "s", "d"]:
            old_row = self.player.row
            old_column = self.player.column
            self.player.move_player(key)
            if self.wall.is_move_valid(self.player):
                self.player.get_energy(resting = False)
                self.message = ""
            else:
                self.player.row = old_row
                self.player.column = old_column
                self.player.get_energy(resting = False)
                self.message = "Invalid move!"
        elif key == "r":
            self.player.get_energy(resting = True)
            self.message = "You rest and gain energy!"
        else:
            self.message = "Invalid input."

    def check_win(self):
        return self.player.row == 0
    def check_game_over(self):
        return self.player.energy <= 0
    def game_loop(self):
        def main(stdscr):
            curses.curs_set(0)
            stdscr.nodelay(False)
            while True:
                stdscr.clear()
                for i in range(self.wall.height):
                    row = ""
                    for j in range(self.wall.width):
                        if self.player.row == i and self.player.column == j:
                            row += "P "
                        elif self.wall.holds[i][j]:
                            row += "H "
                        else:
                            row += ". "
                    stdscr.addstr(i, 0, row)
                stdscr.addstr(self.wall.height + 1, 0, f"Energy: {self.player.energy}")
                stdscr.addstr(self.wall.height + 2, 0, self.message)
                stdscr.refresh()

                key = stdscr.getch()

                if key == ord('w'):
                    self.key_press('w')
                elif key == ord('a'):
                    self.key_press('a')
                elif key == ord('s'):
                    self.key_press('s')
                elif key == ord('d'):
                    self.key_press('d')
                elif key == ord('r'):
                    self.key_press('r')
                elif key == ord('q'):
                    break
                if self.check_win():
                    stdscr.addstr(self.wall.height + 3, 0, "Congratulations! You have reached the top!")
                    stdscr.refresh()
                    curses.napms(2000)
                    break
                if self.check_game_over():
                    stdscr.addstr(self.wall.height + 3, 0, "Game Over! You have run out of energy.")
                    stdscr.refresh()
                    curses.napms(2000)
                    break
        curses.wrapper(main)

class Wall:
    def __init__(self):
        self.height = 10
        self.width = 10
        self.holds = self.generate_wall()
    def generate_wall(self):
        holds = [[False for _ in range(self.width)] for _ in range(self.height)]
        row, column = self.height - 1, 0
        holds[row][column] = True

        while row > 0:
            if column < self.width - 1 and random.random() < 0.5:
                column += 1
            else:
                row -= 1
            holds[row][column] = True
        for i in range(self.height):
            for j in range(self.width):
                if random.random() < 0.3:
                    holds[i][j] = True
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

