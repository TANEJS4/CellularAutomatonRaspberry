# %%
# from simulate import Simulate
# game1 = Simulate(boardSize=100)
# print(game1.run_simulation(n_generations=500))
# %%
from gameboard import GameBoard
from conwayGameoflife import GameOfLife

from matplotlib.animation import FuncAnimation
from highlife import HighLife
import time
import matplotlib.pyplot as plt

SCREEN_WIDTH = 5
SCREEN_HEIGHT = 10
CELL_SIZE = 1


# board = GameBoard(boardSize=5, type="full")
# print("Initial state\n\n", board)
# print(conway.board[0,0])
# print(conway.next_generation())
class Test:
    def __init__(self) -> None:
        self.game = GameOfLife(SCREEN_HEIGHT, alive_prob=0.2)
        self.age = 0
        self.no_progress = False
        while self.age < 100 and not self.no_progress:
            time.sleep((1 / 10))
            if self.age > 10:
                self.game.survival_generation()
            else:
                self.game.next_generation()
            self.age += 1
            self.no_progress = self.game.endgame or self.game.stale
            print(self.game)
            print(
                f"stale progress { self.game.endgame , self.game.stale, self.game.endgame or self.game.stale}"
            )


Test()
