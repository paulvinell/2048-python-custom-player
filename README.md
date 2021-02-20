# 2048-python-custom-player

This is a fork of [2048-python](https://github.com/yangshun/2048-python), by [Yanghun Tay](http://github.com/yangshun).

The point of this implementation is to separate game graphics, logic, and player in such a way that it is easy to automate the game. This version will purposely not have any concept of winning, only losing, and the game stops execution when you lose.

# How do I use this as is?

To start the game, run:

```
$ python main.py
```

Unless modified, you will be given the option to play manually, or watch an automated player making random moves.

# How do I make a custom player?

Custom players must implement the following methods:

* game_grid_init(self, game_grid)
  * called when the graphical representation of the game is initialized.
* play(self, game)
  * called when the player should decide which move to make.
* lost(self, game)
  * called when the player has lost.
* sleep(self, game, render)
  * called after a move has been made, good for looking at an automated player play, or for making games as instant as possible (for training/testing purposes).

I recommend you look at **players/rand_player.py** and **players/manual_player.py** for further details.

# How do I use my custom player?

You instantiate your player, and create and start a "tie in."

```
player = YourPlayer()
tie = TieIn(player, render=True)
tie.start()
```
