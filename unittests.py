import unittest as ut
import board
import numpy as np


class TestBoard(ut.TestCase):

    def test_LegalMove(self):
        testarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        playingboard = board.Board(testarray)

        self.assertEqual(playingboard.LegalMove(0, 0, 6), True)
        self.assertEqual(playingboard.LegalMove(0, 0, 3), False)
        self.assertEqual(playingboard.LegalMove(0, 0, 4), False)
        self.assertEqual(playingboard.LegalMove(0, 0, 1), False)
        self.assertEqual(playingboard.LegalMove(2, 2, 3), False)

    def test_IsEmpty(self):
        testarray = np.array([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
        playingboard = board.Board(testarray)

        self.assertEqual(playingboard.IsEmpty(1, 0), True)
        self.assertEqual(playingboard.IsEmpty(0, 0), False)

    def test_Insert(self):
        testarray = np.array([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
        playingboard = board.Board(testarray)
        playingboard.Insert(2, 1, -1)

        self.assertEqual(playingboard.grid[1][2], -1)

        playingboard.Insert(2, 1, 12)

        self.assertEqual(playingboard.grid[1][2], 12)
