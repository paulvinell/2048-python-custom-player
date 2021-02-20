from players.manual_player import ManualPlayer
from players.rand_player import RandomPlayer

from tie_in import TieIn

def main():
    print("Choose a player:")
    print("1. Manual")
    print("2. Random moves")
    player_int = input()

    if player_int == "1":
        player = ManualPlayer()
    elif player_int == "2":
        player = RandomPlayer()

    tie = TieIn(player, render=True, log_history=False)
    tie.start()

if __name__ == '__main__':
    main()
