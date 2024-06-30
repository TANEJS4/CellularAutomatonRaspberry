import numpy as np
from typing import Self
from gameboard import GameBoard
from copy import deepcopy

from scipy.signal import convolve2d


class GameOfLife(GameBoard):
    def __init__(self, boardSize: int, type="random", alive_prob: float = 0.01):
        GameBoard.__init__(self, boardSize, type, alive_prob)
        self._stale = self.stale_mate()

    @property
    def stale(self):
        self._stale = self.stale_mate()
        return self._stale

    # Functional methods
    def next_generation(self, output_fmt="board") -> Self:
        k = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        n_neighbors = convolve2d(self.board, k, mode="same")

        # Applying the rules to the entire board
        born = (n_neighbors == 3) & (self.board == 1)
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

    # Helper
    def stale_mate(self):
        predict = deepcopy(self)
        
        predict_next = deepcopy(self)
        predict = predict.next_generation()
        predict_next = predict_next.next_generation().next_generation()
        return np.array_equal(predict.board, predict_next.board)
