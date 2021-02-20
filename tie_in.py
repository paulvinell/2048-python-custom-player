import threading
import time

from game import Game
from game_grid import GameGrid
from players.manual_player import ManualPlayer
from players.rand_player import RandomPlayer

class TieIn():
    def __init__(self, player, render=True, log_history=False):
        self.game = Game(log_history=log_history)
        self.player = player
        self.render = render

        if self.player is None:
            self.player = ManualPlayer()

        if self.render:
            self.game_grid = GameGrid(self.game)
            self.player.game_grid_init(self.game_grid)

    def start(self):
        self.gamethread = threading.Thread(target=self.__gameloop)
        self.gamethread.start()

        if self.render:
            self.game_grid.mainloop()

    def __gameloop(self):
        while True:
            response = self.player.play(self.game) # Ask for player input

            changed = self.game.make_move(response) # Try to perform the move

            if changed:
                if self.render:
                    self.game_grid.update_grid_cells(self.game) # Render if we're supposed to

                if not self.game.alive():
                    self.player.lost(self.game)
                    break # Quit the game loop if the game is over

                sleep_time = self.player.sleep(self.game, self.render)
                if sleep_time > 0:
                    time.sleep(sleep_time) # Sleeping can be necessary to visualize automated agents playing
