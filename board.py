import numpy as np


class Board():
    def __init__(self, array):
        self.grid = array

    def LegalMove(self, x, y, n):
        """
        Determines whether placing the given number on the given location in the grid would be a legal move
        @param x: (int) x coordinate for placement location
        @param y: (int) y coordinate for placement location
        @param n: (int) number to place
        """

        if n in self.grid[y]:
            return False
        elif n in self.grid[:, x]:
            return False
        else:
            x_box = x // 3
            y_box = y // 3
            for i in range(x_box * 3, x_box * 3 + 3):
                for j in range(y_box * 3, y_box * 3 + 3):
                    if self.grid[j][i] == n:
                        return False
            return True

    def IsEmpty(self, x, y):
        """
        Determines whether a given location on the board is empty, i.e. has a 0 as value
        @param x: (int) x coordinate for location to check
        @param y: (int) y cooridnate for location to check
        """
        if self.grid[y][x] == 0:
            return True
        else:
            return False

    def Insert(self, x, y, n):
        """
        Inserts the given number in the given location on the grid
        @param x: (int) x coordinate for insertion location
        @param y: (int) y coordinate for insertion location
        @param n: (int) number to insert
        """
        self.grid[y][x] = n

    def Solve(self):
        """
        Solves the instance of the board by using a backtracking algorithm
        Prints the solved board
        """
        for x in range(9):
            for y in range(9):
                if self.IsEmpty(x, y):
                    for n in range(1, 10):
                        if (self.LegalMove(x, y, n)):
                            self.Insert(x, y, n)
                            self.Solve()
                            self.Insert(x, y, 0)
                    return
        self.PrintBoard()

    def PrintBoard(self):
        """
        Prints the board in a readable manner
        """
        print(self.grid)
