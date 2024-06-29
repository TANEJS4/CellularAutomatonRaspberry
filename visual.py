from re import S
import pyxel

from gameboard import GameBoard
from conwayGameoflife import GameOfLife

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
CELL_SIZE = 4

class Board:
    def __init__(self, type="Conways", **args):
        self.game = GameOfLife(boardSize = 256, **args)
        

    def update(self):
        self.game.updateNeighbors()


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="CellularAutomaton", capture_scale=1)
        pyxel.mouse(True)

        self.board = GameBoard(256,"Random", alive_prob= 0.2)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
    def draw(self):
        pyxel.cls(0)

        for i in range (SCREEN_HEIGHT):
            for j in range(SCREEN_WIDTH):
                pyxel.rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE, self.board[(i,j)])
App()