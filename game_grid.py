from tkinter import Frame, Label, CENTER

import constants as c
from game import Game

class GameGrid(Frame):
    def __init__(self, game):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<KeyPress>", self.key_down)
        self.master.bind("<KeyRelease>", self.key_up)

        self.grid_cells = []
        self.keys = {} # Which keys are currently being pressed?

        self.init_grid()
        self.update_grid_cells(game)

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

    def update_grid_cells(self, game):
        for i in range(c.GRID_LEN_Y):
            for j in range(c.GRID_LEN_X):
                new_number = game.matrix[i][j]
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
