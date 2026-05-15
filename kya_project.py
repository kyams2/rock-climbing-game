import random
import curses
import time
MAX_LEVEL = 10

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
            self.energy += 4 #gain energy
        else:
            self.energy -= 1 #lose energy

class Game:
    def __init__(self):
        self.wall = Wall()
        self.player = Player(self.wall.height - 1, 0)
        self.wall.holds[self.wall.height - 1][0] = 1
        self.message = ""
        self.rests_left = 3
        self.start_time = time.time()
        self.discovered = set()
        self.level = 1
    def next_level(self):
        self.level += 1
        self.wall = Wall(height = min(10 + self.level * 2, 30), width = min(10 + self.level, 30), difficulty = self.level)
        self.player.row = self.wall.height - 1
        self.player.column = 0
        self.wall.holds[self.player.row][self.player.column] = 1
        self.player.energy = 15 + self.level * 2
        self.rests_left = 3
        self.discovered.clear()
        self.message = f"Welcome to Level {self.level}!"
    def key_press(self, key):
        if key in ["w", "a", "s", "d"]:
            old_row = self.player.row
            old_column = self.player.column
            self.player.move_player(key)
            if self.wall.is_move_valid(self.player):
                tile = self.wall.holds[self.player.row][self.player.column]
                self.discovered.add((self.player.row, self.player.column))
                self.player.energy -= 1
                if tile == 1:
                    self.message = ""
                elif tile == 2:
                    self.player.energy -= 1
                    self.message = "Bad Hold!"
                elif tile == 3:
                    self.player.energy += 3
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
            max_y, max_x = stdscr.getmaxyx()
            curses.curs_set(0)
            stdscr.nodelay(True)
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
                        elif tile != 0:
                            if (i, j) in self.discovered:
                                if tile == 1:
                                    row += "H "
                                elif tile == 2:
                                    row += "E "
                                elif tile == 3:
                                    row += "R "
                            else:
                                row += "O "
                    if i < max_y:
                        stdscr.addstr(i, 0, row[:max_x - 1])
                elapsed_time = int(time.time() - self.start_time)
                minutes = elapsed_time // 60
                seconds = elapsed_time % 60
                if self.wall.height + 1 < max_y:
                    stdscr.addstr(self.wall.height + 1, 0, f"Energy: {self.player.energy}" [:max_x - 1])
                if self.wall.height + 2 < max_y:
                    stdscr.addstr(self.wall.height + 2, 0, f"Rests Left: {self.rests_left}" [:max_x - 1])
                if self.wall.height + 3 < max_y:
                    stdscr.addstr(self.wall.height + 3, 0, self.message[:max_x - 1])
                if self.wall.height + 4 < max_y:
                    stdscr.addstr(self.wall.height + 4, 0, f"Time: {minutes:02}:{seconds:02}"[:max_x - 1])

                stdscr.refresh()
                time.sleep(0.05)
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
                    if self.level >= MAX_LEVEL:
                        stdscr.addstr(self.wall.height + 3, 0, "Congratulations! You have reached the top of the mountain!")
                        stdscr.refresh()
                        curses.napms(3000)
                        break
                    stdscr.addstr(self.wall.height + 3, 0, f"Level {self.level} Complete! Onward!")
                    stdscr.refresh()
                    curses.napms(1500)
                    self.next_level()
                if self.check_game_over():
                    stdscr.addstr(self.wall.height + 3, 0, "Game Over! You have run out of energy.")
                    stdscr.refresh()
                    curses.napms(2000)
                    break
        curses.wrapper(main)

class Wall:
    def __init__(self, height = 10, width = 10, difficulty = 1):
        self.height = height
        self.width = width
        self.difficulty = difficulty
        self.holds = self.generate_wall()
    def generate_wall(self):
        holds = [[0 for _ in range(self.width)] for _ in range(self.height)]
        row, column = self.height - 1, 0
        holds[row][column] = 1
        
        while row > 0:
            if column < self.width - 1 and random.random() < 0.5:
                column += 1
            else:
                row -= 1
            holds[row][column] = 1
        bad_hold_chance = min(0.15 + self.difficulty * 0.02, 0.40)
        rest_hold_chance = max(0.10 - self.difficulty * 0.01, 0.05)
        normal_hold_chance = 0.35
        for i in range(self.height):
            for j in range(self.width):
                if holds[i][j] == 1:
                    continue
                r = random.random()
                if r < bad_hold_chance:
                    holds[i][j] = 2
                elif r < bad_hold_chance + rest_hold_chance:
                    holds[i][j] = 3
                elif r < bad_hold_chance + rest_hold_chance + normal_hold_chance:
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

