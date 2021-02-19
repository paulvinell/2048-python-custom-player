import time

class ManualPlayer():
    def __init__(self, game_frame):
        self.game_frame = game_frame

    def play(self, matrix):
        while True:
            if 'w' in self.game_frame.keys and self.game_frame.keys['w']:
                self.game_frame.keys['w'] = False
                return 0
            elif 'a' in self.game_frame.keys and self.game_frame.keys['a']:
                self.game_frame.keys['a'] = False
                return 2
            elif 's' in self.game_frame.keys and self.game_frame.keys['s']:
                self.game_frame.keys['s'] = False
                return 1
            elif 'd' in self.game_frame.keys and self.game_frame.keys['d']:
                self.game_frame.keys['d'] = False
                return 3

            time.sleep(0.01)

        return -1

    def lost(self, game):
        print("Lost!")
        print("Made {} moves".format(game.move_count))
        print("Maximum tile was {}".format(game.max_tile))

    def sleep(self, matrix):
        return 0
