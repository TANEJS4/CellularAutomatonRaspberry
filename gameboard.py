from typing import Self
import numpy as np
import numpy.typing as npt

class GameBoard:
    def __init__(self, boardSize: int, type="random", alive_prob: float = 0.1):
        self.boardSize = boardSize
        self._board = self._generateBoard(type, alive_prob)
        self._endgame =  self.endgame_state()
    
    @property
    def board(self):
        return self._board
    @property
    def endgame(self):
        return self._endgame

    @board.setter
    def board(self, new_board):
        self._board = new_board
        self._endgame = self.endgame_state()

    def __getitem__(self, tup):
        i, j = tup
        return self._board[i][j]
    def _generateBoard(self, type, alive_prob) -> npt.NDArray[np.float64]:
        if type == "full":
            return np.ones((self.boardSize, self.boardSize))
        elif type == "empty":
            return np.zeros((self.boardSize, self.boardSize))
        else:
            return np.random.choice(
                a=[0, 1],
                size=(self.boardSize, self.boardSize),
                p=[1 - alive_prob, alive_prob],
            )
    
    
    def endgame_state(self) -> bool:
        return not any(any(row) for row in self._board)


    def __str__(self) -> str :
        out = ""
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                out += " o " if self.board[i][j] != 0.0 else " - "
            out += "\n"
        return out
 