# %%
# from simulate import Simulate
# game1 = Simulate(boardSize=100)
# print(game1.run_simulation(n_generations=500))
# %%
from gameboard import GameBoard
from conwayGameoflife import GameOfLife
from highlife import HighLife
SCREEN_WIDTH = 5
SCREEN_HEIGHT = 5
CELL_SIZE = 1

# board = GameBoard(boardSize=5, type="full")
# print("Initial state\n\n", board)
# print(conway.board[0,0])
# print(conway.next_generation())
class Test:
    def __init__(self) -> None:
        self.game = GameOfLife(5, type="full")
        print(self.game)
        print("stale",self.game.stale)

        self.game.next_generation()
        print(self.game)
        print("stale",self.game.stale)


Test()