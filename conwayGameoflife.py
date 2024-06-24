import numpy as np
import numpy.typing as npt

from scipy.signal import convolve2d

class GameOfLife :

    @staticmethod
    def updateNeighbors(curr_board: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        k = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1]])
        n_neighbors = convolve2d(curr_board, k, mode='same')
        print("n_neighbors", n_neighbors)

        # Applying the rules to the entire board
        born = (n_neighbors == 3) & (curr_board == 1)
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (curr_board == 0)
        new_board = born | survive

        return new_board.astype(float)

