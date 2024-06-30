import time

import pyxel as px

from conwayGameoflife import GameOfLife
from highlife import HighLife

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
TEXT_POS_X = SCREEN_WIDTH / 2 - SCREEN_WIDTH / 10
TEXT_POS_Y = SCREEN_HEIGHT / 2
TEXT_POS_CORNER_X = 10
TEXT_POS_CORNER_Y = SCREEN_HEIGHT - 10
CELL_SIZE = 4

# GAME STATE
PLAYING = 1
MENU = -1
PAUSED = 0
TEXT_COLOR = 11


class Board:
    def __init__(self):
        self.game_types = [GameOfLife, HighLife]
        self.game = GameOfLife(SCREEN_HEIGHT)
        self.fps = 5
        self.state = MENU
        self.age = 0
        self.no_progress = False
        px.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="CellularAutomaton", fps=self.fps)
        # px.mouse(True)
        px.run(self.update, self.draw)

    def update(self):
        # * quit game
        if px.btnp(px.KEY_Q):
            px.quit()

        # * set game state
        if self.state != PLAYING and px.btnp(px.KEY_R):
            self.state = PLAYING
        if px.btnp(px.KEY_P):
            self.state = PAUSED
        if px.btnp(px.KEY_M):
            self.state = MENU

        if self.no_progress or self.age > 100:
            self.age = 0
            self.no_progress = False
            self.game = GameOfLife(SCREEN_HEIGHT)

        self.no_progress = self.game.endgame or self.game.stale_mate()
        # * update game
        if self.state == PLAYING:
            time.sleep((1 / self.fps) * 3)
            if self.age > 50:
                self.game.survival_generation()
            else:
                self.game.next_generation()
            self.age += 1

    def menu(self):
        px.text(TEXT_POS_X, TEXT_POS_Y - 30, "cellular automaton", TEXT_COLOR)
        px.text(TEXT_POS_X, TEXT_POS_Y, "P to Pause the game", TEXT_COLOR)
        px.text(
            TEXT_POS_X, TEXT_POS_Y + 20, "R or Left Click to run the game", TEXT_COLOR
        )
        px.text(TEXT_POS_X, TEXT_POS_Y + 40, "M to enter menu", TEXT_COLOR)

    def stats(self):
        px.text(
            TEXT_POS_CORNER_X,
            TEXT_POS_CORNER_Y,
            f"Generation: {self.age}",
            self.age % 16 + 1,
        )
        px.text(
            TEXT_POS_CORNER_X,
            TEXT_POS_CORNER_Y - 10,
            f"no_progress: {self.game.endgame , self.no_progress,self.game.endgame or self.game.stale }",
            self.age % 16 + 1,
        )

    def draw(self):
        px.cls(0)
        if self.state == MENU:
            self.menu()
        else:  # px.
            for i in range(SCREEN_HEIGHT):
                for j in range(SCREEN_WIDTH):
                    px.rect(
                        i * CELL_SIZE,
                        j * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                        int(self.game.board[i, j]) * 15,
                    )
            self.stats()


Board()
