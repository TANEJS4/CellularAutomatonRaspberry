import numpy as np
import numpy.typing as npt

from scipy.signal import convolve2d
# from gameboard import GameBoard
class GameOfLife :
    # def __init__(self):
    #     self.board = board

    @staticmethod
    def updateNeighbors(curr_board: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        k = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])
        n_neighbors = convolve2d(curr_board, k, mode='same')

        # Applying the rules to the entire board
        born = (n_neighbors == 3) & (curr_board == 0)
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (curr_board == 1)
        new_board = born | survive

        return new_board.astype(float)

