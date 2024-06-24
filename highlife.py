import numpy as np
import numpy.typing as npt
from scipy.signal import convolve2d
from gameboard import GameBoard
class HighLife (GameBoard):

    # @staticmethod
    def updateNeighbors(self) ->  npt.NDArray[np.float64]:
    #  curr_board: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        curr_board =  self.board
        k = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])
        n_neighbors = convolve2d(curr_board, k, mode='same')

        # Applying the rules to the entire board
        born = (n_neighbors == 3) | (n_neighbors == 6)  & (curr_board == 1)
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (curr_board ==0)
        new_board = born | survive

        return new_board.astype(float)
