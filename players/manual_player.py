import time

class ManualPlayer():
    def game_grid_init(self, game_grid):
        self.game_grid = game_grid

    def play(self, game):
        while True:
            if 'w' in self.game_grid.keys and self.game_grid.keys['w']:
                self.game_grid.keys['w'] = False
                return 0
            elif 'a' in self.game_grid.keys and self.game_grid.keys['a']:
                self.game_grid.keys['a'] = False
                return 2
            elif 's' in self.game_grid.keys and self.game_grid.keys['s']:
                self.game_grid.keys['s'] = False
                return 1
            elif 'd' in self.game_grid.keys and self.game_grid.keys['d']:
                self.game_grid.keys['d'] = False
                return 3

            time.sleep(0.01)

        return -1

    def lost(self, game):
        print("Lost!")
        print("Number of moves: {}".format(game.move_count))
        print("Maximum tile: {}".format(game.max_tile))
        print("Score: {}".format(game.score))

    def sleep(self, game, render):
        return 0
