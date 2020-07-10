import board
import numpy as np

grid = np.array([[0, 4, 0, 9, 0, 2, 0, 0, 8],
                 [0, 3, 7, 8, 0, 0, 0, 0, 0],
                 [0, 0, 9, 0, 0, 1, 0, 0, 6],
                 [0, 0, 0, 0, 0, 8, 0, 1, 0],
                 [0, 0, 0, 2, 0, 0, 0, 0, 7],
                 [0, 0, 1, 6, 7, 3, 0, 0, 4],
                 [8, 0, 0, 0, 0, 0, 4, 0, 0],
                 [4, 9, 0, 0, 0, 0, 0, 2, 0],
                 [0, 1, 2, 0, 8, 0, 3, 0, 5]])


playingboard = board.Board(grid)
print("Board to solve:")
playingboard.PrintBoard()
print("Solved:")
playingboard.Solve()
