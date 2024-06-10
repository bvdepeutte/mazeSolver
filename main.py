from maze import Maze
from cell import Cell
from graphics import Window,Point,Line

def main():
    win = Window(800,600)
    point1=Point(10,10)
    point2=Point(100,100)
    cell1=Cell(point1.x,point1.y,point2.x,point2.y,win)
    cell1.draw()
    win.waitForClose()

if __name__ == "__main__":
    main()