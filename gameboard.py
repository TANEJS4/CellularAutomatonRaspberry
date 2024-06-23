import numpy as np
import numpy.typing as npt

class GameBoard:
    def __init__(self, boardSize: int, type="random", alive_prob: float = 0.1):
        self.boardSize = boardSize
        self.board = self.generateBoard(type, alive_prob)
    
    
    def generateBoard(self, type, alive_prob) -> npt.NDArray[np.float64]:
        if type == "full":
            return np.ones((self.boardSize, self.boardSize))
        elif type == "empty":
            return np.zeros((self.boardSize, self.boardSize))
        # else type == "random":
        return np.random.choice(
            a=[0, 1],
            size=(self.boardSize, self.boardSize),
            p=[1 - alive_prob, alive_prob],
        )

    def generateBoardState(self):
        return

    def __str__(self) -> str :
        out = ""
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                out += " o " if self.board[i][j] != 0.0 else " - "
            out += "\n"
        return out
 