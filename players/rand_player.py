import numpy as np

class RandomPlayer():
    def play(self, matrix):
        return np.random.randint(0, high=4)

    def lost(self, game):
        print("Lost!")

    # Go slower when the action gets cooler
    def sleep(self, matrix):
        highest_grid_tile = 0
        for col in matrix:
            for elem in col:
                if elem > highest_grid_tile:
                    highest_grid_tile = elem
        return (np.log2(highest_grid_tile) / 17) / 2
