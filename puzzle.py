import random
from tkinter import Frame, Label, CENTER

import threading
import time
import constants as c
import numpy as np
from game import Game

from players.manual_player import ManualPlayer
from players.rand_player import RandomPlayer

# TODO: keep track of number of moves (excluding moves that don't affect anything)
# TODO: completely separate game logic, rendering, and player

class GameGrid(Frame):
    def __init__(self, render=True, player=None):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<KeyPress>", self.key_down)
        self.master.bind("<KeyRelease>", self.key_up)

        self.game = Game()

        self.grid_cells = []
        self.keys = {} # Which keys are currently being pressed?
        self.render = render # Boolean - whether or not to render

        self.init_grid()
        self.update_grid_cells()

        if player is None:
            # self.player = RandomPlayer()
            self.player = ManualPlayer(self)

        self.gamethread = threading.Thread(target=self.gameloop)
        self.gamethread.start()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN_Y):
            grid_row = []
            for j in range(c.GRID_LEN_X):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN_X,
                             height=c.SIZE / c.GRID_LEN_Y)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN_Y):
            for j in range(c.GRID_LEN_X):
                new_number = self.game.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = event.keysym
        self.keys[key] = True

    def key_up(self, event):
        key = event.keysym
        self.keys[key] = False

    def gameloop(self):
        while True:
            response = self.player.play(self.game.matrix) # Ask for player input

            changed = self.game.make_move(response) # Try to perform the move

            if changed:
                if self.render:
                    self.update_grid_cells() # Render if we're supposed to

                if not self.game.alive():
                    self.player.lost(self.game)
                    break # Quit the game loop if the game is over

                sleep_time = self.player.sleep(self.game.matrix)
                if sleep_time > 0:
                    time.sleep(sleep_time) # Sleeping can be necessary to visualize automated agents playing

if __name__ == '__main__':
    gamegrid = GameGrid()
