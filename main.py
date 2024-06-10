from maze import Maze
from cell import Cell
from graphics import Window,Point,Line

def main():
        numCols = 5
        numRows = 5
        win = Window(200,200)
        m1 = Maze(10, 10, numRows, numCols, 10, 10, win)
        m1.breakEntranceAndExit()
        win.waitForClose()

if __name__ == "__main__":
    main()