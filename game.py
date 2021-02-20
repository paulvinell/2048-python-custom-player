import random
import numpy as np
import copy
import constants as c

class Game():
    def __init__(self, log_history=False):
        self.move_count = 0
        self.max_tile = 0
        self.score = 0

        self.log_history = log_history
        if self.log_history:
            self.move_history = []
            self.board_history = []

        self.matrix = self.__init_matrix()

    def make_move(self, move):
        game = self.matrix
        game_copy = copy.deepcopy(game)

        if move == 0:
            game = self.__up(game)
        elif move == 1:
            game = self.__down(game)
        elif move == 2:
            game = self.__left(game)
        elif move == 3:
            game = self.__right(game)

        changed = not np.array_equal(game, game_copy)

        # Case 1: there was no change: don't add a tile
        # Case 2: board was full and there was a change:
        # at least one tile has been merged, and there is space for more.
        # Case 3: board was not full and there was a change:
        # there was and is space for more.
        if changed:
            game = self.__add_two(game)
            self.move_count += 1
            if self.log_history:
                self.move_history.append(move)
                self.board_history.append(game_copy)

            self.matrix = game

        return changed

    # In this variant, there is only Lost/Not lost.
    def alive(self):
        game = self.matrix

        for i in range(len(game)):  # check for any zero entries
            for j in range(len(game[0])):
                if game[i][j] == 0:
                    return True

        for i in range(len(game)): # Check across x/columns
            for j in range(len(game[0]) - 1):
                if game[i][j] == game[i][j+1]:
                    return True

        for j in range(len(game[0])): # Check across y/rows
            for i in range(len(game) - 1):
                if game[i][j] == game[i+1][j]:
                    return True

        return False

    # Creates a game board of dimensions
    # specified in Constants and adds
    # two starting tiles.
    def __init_matrix(self):
        matrix = []

        for i in range(c.GRID_LEN_Y):
            matrix.append([0] * c.GRID_LEN_X)

        matrix = self.__add_two(matrix)
        matrix = self.__add_two(matrix)

        return matrix

    # Adds a two or four tile to an empty slot
    def __add_two(self, mat):
        empty = []
        for a, col in enumerate(mat):
            for b, elem in enumerate(col):
                if elem == 0:
                    empty.append((a, b))

        if len(empty) == 0:
            return mat

        a, b = random.choice(empty)
        value = 4 if random.random() <= c.PROBABILITY_4 else 2

        mat[a][b] = value
        self.max_tile = np.maximum(self.max_tile, value)

        return mat

    # Calculates which directions it is possible to move in
    def possible_directions(self):
        directions = []
        mat = self.matrix

        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > 0 and (mat[i][j] == mat[i-1][j] or mat[i-1][j] == 0):
                    directions.append(0) # UP
                    break

            if 0 in directions:
                break

        for i in range(len(mat) - 1):
            for j in range(len(mat[0])):
                if mat[i][j] > 0 and (mat[i][j] == mat[i+1][j] or mat[i+1][j] == 0):
                    directions.append(1) # DOWN
                    break

            if 1 in directions:
                break

        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] > 0 and (mat[i][j] == mat[i][j-1] or mat[i][j-1] == 0):
                    directions.append(2) # LEFT
                    break

            if 2 in directions:
                break

        for i in range(len(mat)):
            for j in range(len(mat[0]) - 1):
                if mat[i][j] > 0 and (mat[i][j] == mat[i][j+1] or mat[i][j+1] == 0):
                    directions.append(3) # RIGHT
                    break

            if 3 in directions:
                break

        return directions

    def __reverse(self, mat):
        new = []
        for i in range(len(mat)):
            new.append([])
            for j in range(len(mat[0])):
                new[i].append(mat[i][len(mat[0])-j-1])
        return new

    def __transpose(self, mat):
        new = []
        for i in range(len(mat[0])):
            new.append([])
            for j in range(len(mat)):
                new[i].append(mat[j][i])
        return new

    def __cover_up(self, mat):
        new = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    new[i][count] = mat[i][j]
                    count += 1
        return new


    def __merge(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])-1):
                if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                    mat[i][j] *= 2
                    mat[i][j+1] = 0
                    self.max_tile = np.maximum(self.max_tile, mat[i][j])
                    self.score += mat[i][j]
        return mat

    def __up(self, game):
        game = self.__transpose(game)
        game = self.__cover_up(game)
        game = self.__merge(game)
        game = self.__cover_up(game)
        game = self.__transpose(game)
        return game

    def __down(self, game):
        game = self.__reverse(self.__transpose(game))
        game = self.__cover_up(game)
        game = self.__merge(game)
        game = self.__cover_up(game)
        game = self.__transpose(self.__reverse(game))
        return game

    def __left(self, game):
        game = self.__cover_up(game)
        game = self.__merge(game)
        game = self.__cover_up(game)
        return game

    def __right(self, game):
        game = self.__reverse(game)
        game = self.__cover_up(game)
        game = self.__merge(game)
        game = self.__cover_up(game)
        game = self.__reverse(game)
        return game
