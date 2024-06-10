import unittest

from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def testMazeCreateCells(self):
        numCols = 12
        numRows = 10
        win = Window(100,120)
        m1 = Maze(0, 0, numRows, numCols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            numCols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            numRows,
        )

    def testMazeCreateCellsSmall(self):
        numCols = 5
        numRows = 7
        win = Window(100,120)
        m1 = Maze(0, 0, numRows, numCols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            numCols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            numRows,
        )
    
    def testMazeEntranceAndExit(self):
        numCols = 5
        numRows = 5
        win = Window(200,200)
        m1 = Maze(0, 0, numRows, numCols, 10, 10, win)
        m1.breakEntranceAndExit()
        self.assertTrue(
            m1._cells[0][0].hasLeftWall == False,"Left Top Wall should be broken"
        )
        self.assertTrue(
            m1._cells[numCols-1][numRows-1].hasRightWall == False,"Right bottom Wall should be broken"
        )    
if __name__ == "__main__":
    unittest.main()