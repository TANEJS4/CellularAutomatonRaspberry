# %%
# from simulate import Simulate
# game1 = Simulate(boardSize=100)
# print(game1.run_simulation(n_generations=500))
# %%

from gameboard import GameBoard
from conwayGameoflife import GameOfLife
from highlife import HighLife

# board = GameBoard(boardSize=5, type="full")
# print("Initial state\n\n", board)
conway = HighLife(boardSize=5,  type="full")
print(type(conway))

print(conway.updateNeighbors())
print(conway.endgame)
print((conway.updateNeighbors()))
print(conway.endgame)
print(conway.endgame)
