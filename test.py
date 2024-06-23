# %%
from simulate import Simulate
game1 = Simulate(boardSize=100)
print(game1.run_simulation(n_generations=5))

# board = GameBoard(5)
# print("Initial state\n\n",  board)
# conway = GameOfLife()
# print(conway.updateNeighbors(board))
