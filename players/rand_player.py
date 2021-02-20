import numpy as np

class RandomPlayer():

    # This is called when the graphical representation
    # of the game is initialized.
    # Input: a reference to the frame
    def game_grid_init(self, game_grid):
        pass

    # Input: the game board
    # Output: a digit from [0, 1, 2, 3] signifying direction.
    # 0: UP, 1: DOWN, 2: LEFT, 3: RIGHT
    def play(self, game):
        return np.random.randint(0, high=4)

    # The game is over.
    # Input: game state
    def lost(self, game):
        print("Lost!")
        print("Number of moves: {}".format(game.move_count))
        print("Maximum tile: {}".format(game.max_tile))
        print("Score: {}".format(game.score))

    # Go slower when the action gets cooler,
    # except if we're not rendering.
    # Input: game state, and whether the game is being rendered
    # Output: sleep time (in seconds)
    def sleep(self, game, render):
        if not render:
            return 0

        highest_grid_tile = 0
        for col in game.matrix:
            for elem in col:
                if elem > highest_grid_tile:
                    highest_grid_tile = elem
        return (np.log2(highest_grid_tile) / 17) / 2
