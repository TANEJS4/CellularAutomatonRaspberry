from typing import Self
import numpy as np
from scipy.signal import convolve2d
from gameboard import GameBoard


class HighLife(GameBoard):
    def next_generation(self, output_fmt="board") -> Self:
        #  ->  npt.NDArray[np.float64]

        k = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        n_neighbors = convolve2d(self.board, k, mode="same")

        # Applying the rules to the entire board
        born = (n_neighbors == 3) | (n_neighbors == 6) & (self.board == 1)
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (self.board == 0)
        new_board = born | survive

        self.board = new_board

        return self

    def survival_generation(self, output_fmt="board") -> Self:
        k = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        n_neighbors = convolve2d(self.board, k, mode="same")

        # Applying the rules to the entire board
        survive = ((n_neighbors == 2) | (n_neighbors == 3)) & (self.board == 1)
        new_board = survive
        self.board = new_board
        return self
