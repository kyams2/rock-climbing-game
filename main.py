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
            return
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
        self.rests_left = 3
    def key_press(self, key):
        if key in ["w", "a", "s", "d"]:
            old_row = self.player.row
            old_column = self.player.column
            self.player.move_player(key)
            if self.wall.is_move_valid(self.player):
                tile = self.wall.holds[self.player.row][self.player.column]
                self.player.energy -= 1
                if tile == 1:
                    self.message = ""
                elif tile == 2:
                    self.player.energy -= 2
                    self.message = "Bad Hold!"
                elif tile == 3:
                    self.player.energy += 2
                    self.message = "Rest Hold!"
            else:
                self.player.row = old_row
                self.player.column = old_column
                self.message = "Invalid move!"
        elif key == "r":
            if self.rests_left > 0:
                self.player.energy += 2
                self.rests_left -= 1
                self.message = f"You rest and gain energy! Rests left: {self.rests_left}"
            else:
                self.message = "No rests left!"
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
                        tile = self.wall.holds[i][j]
                        if self.player.row == i and self.player.column == j:
                            row += "P "
                        elif tile == 0:
                            row += ". "
                        elif tile == 1:
                            row += "H "
                        elif tile == 2:
                            row += "E "
                        elif tile == 3:
                            row += "R "
                    stdscr.addstr(i, 0, row)
                stdscr.addstr(self.wall.height + 1, 0, f"Energy: {self.player.energy}")
                stdscr.addstr(self.wall.height + 2, 0, f"Rests left: {self.rests_left}")
                stdscr.addstr(self.wall.height + 3, 0, self.message)
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
        holds = [[0 for _ in range(self.width)] for _ in range(self.height)]
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
                if holds[i][j] == 1:
                    continue
                r = random.random()
                if r < 0.15:
                    holds[i][j] = 2
                elif r < 0.20:
                    holds[i][j] = 3
                elif r < 0.35:
                    holds[i][j] = 1
        return holds
    def is_move_valid(self, player):
        if 0 <= player.row < self.height and 0 <= player.column < self.width:
            return self.holds[player.row][player.column] != 0
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

