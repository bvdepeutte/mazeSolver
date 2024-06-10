from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            numRows,
            numCols,
            cellSizeX,
            cellSizeY,
            win,
        ):
        self.x1 = x1
        self.y1 = y1
        self.numRows = numRows
        self.numCols = numCols
        self.cellSizeX = cellSizeX
        self.cellSizeY = cellSizeY
        self.win = win
        self._createCells()
    
    def _createCells(self):
        self._cells = []
        rows = []
        for col in range(0,self.numCols):
            rows = []
            for row in range(0,self.numRows):
                x = self.x1 + col * self.cellSizeX
                y = self.y1 + row * self.cellSizeY
                rows.append(Cell(x,y,x+self.cellSizeX,y+self.cellSizeY,self.win))
            self._cells.append(rows)
        
        for col in range(self.numCols):
            for row in range(self.numRows):
                self._drawCell(col, row)
    
    def _drawCell(self,col,row):
        x = self.x1 + col * self.cellSizeX
        y = self.y1 + row * self.cellSizeY
        cell = self._cells[col][row]
        cell.draw()
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
