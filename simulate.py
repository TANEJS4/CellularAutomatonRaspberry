# %%

from matplotlib import color_sequences
import matplotlib.pyplot as plt

from gameboard import GameBoard
from conwayGameoflife import GameOfLife
from matplotlib.animation import FuncAnimation
from PIL import Image
# board = GameBoard(5)
# print("Initial state\n\n",  board)
# conway = GameOfLife()
# print(conway.next_generation(board))

class Simulate:
    def __init__(self, boardSize :int ,game =  "conway"):
        self.board = GameBoard(boardSize)
        self.game = GameOfLife()
    
    # https://matplotlib.org/3.1.0/tutorials/colors/colormap-manipulation.html
    def setColorSchema(self, colormap, ax ):
        pass

    def run_simulation(self, n_generations):
            # Initialize a figure for plotting
            board_map = self.board.board
            fig, ax = plt.subplots()
            ax.set_axis_off()
            fig.set_facecolor("#000000")
            img = ax.imshow(board_map,animated=True,cmap="copper")
            # img.cmap = "plasma"
            
            def update(frame):
                nonlocal board_map
                if frame > 0:
                    board_map = self.game.next_generation(board_map)
                img.set_data(board_map)
                return [img]

            print("Compiling the frames to video format...")
            animated_board = FuncAnimation(
                fig,
                update,
                frames=n_generations,
                blit=True,
                interval=1000,
                # repeat_delay=100
            )
            # animated_board.
            plt.close()

            print("Saving animation as: run")
            animated_board.save("run.mp4", fps=24)