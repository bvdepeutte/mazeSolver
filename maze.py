from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            numRows,
            numCols,
            cellSizeX,
            cellSizeY,
            win=None,
            seed = None
        ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.numRows = numRows
        self.numCols = numCols
        self.cellSizeX = cellSizeX
        self.cellSizeY = cellSizeY
        self.win = win
        if seed:
            random.seed(seed)

        self._createCells()
        self.breakEntranceAndExit()
        self._breakWallsR(0, 0)
        self._resetCellsVisited()
    
    def _createCells(self):
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
        if self.win is None:
            return
        x1 = self.x1 + col * self.cellSizeX
        y1 = self.y1 + row * self.cellSizeY
        x2 = x1 + self.cellSizeX
        y2 = y1 + self.cellSizeY
        self._cells[col][row].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def breakEntranceAndExit(self):
        col = self.numCols - 1
        row = self.numRows - 1
        self._cells[0][0].hasLeftWall = False
        self._drawCell(0,0)
        self._cells[col][row].hasRightWall = False
        self._drawCell(col,row)
    
    def _breakWallsR(self,i,j):
        self._cells[i][j].visited = True
        while True:
            toVisit = []
            cellToVisit = ()
            if i < self.numCols -1 and not self._cells[i+1][j].visited:
                cellToVisit = (i+1,j,"right")                
                toVisit.append(cellToVisit)
            if i > 0 and not self._cells[i-1][j].visited:
                cellToVisit = (i-1,j,"left")
                toVisit.append(cellToVisit)
            if j > 0 and not self._cells[i][j-1].visited:
                cellToVisit = (i,j-1,"top")
                toVisit.append(cellToVisit)
            if j < self.numRows - 1 and not self._cells[i][j+1].visited:
                cellToVisit = (i,j+1,"bot")
                toVisit.append(cellToVisit)
            
            if len(toVisit) == 0:
                self._drawCell(i,j)
                return
            
            direction = random.choice(toVisit)
        
            if direction[2] == "right":
                self._cells[i][j].hasRightWall = False
                self._cells[i+1][j].hasLeftWall = False
            elif direction[2] == "left":
                self._cells[i][j].hasLeftWall = False
                self._cells[i-1][j].hasRightWall = False
            elif direction[2] == "top":
                self._cells[i][j].hasTopWall = False
                self._cells[i][j-1].hasBotWall = False
            elif direction[2] == "bot":
                self._cells[i][j].hasBotWall = False
                self._cells[i][j+1].hasTopWall = False
            
            self._breakWallsR(direction[0],direction[1])
    
    def _resetCellsVisited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solveR(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self.numCols -1 and j == self.numRows -1:
            return True
        
        # move left
        if(
            i> 0
            and not self._cells[i][j].hasLeftWall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].drawMove(self._cells[i-1][j])
            if self.solveR(i-1,j):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i-1][j],True)
        
        # move right
        if(
            i < self.numCols - 1
            and not self._cells[i][j].hasRightWall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].drawMove(self._cells[i+1][j])
            if self.solveR(i+1,j):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i+1][j],True)

        # move top
        if(
            j> 0
            and not self._cells[i][j].hasTopWall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].drawMove(self._cells[i][j-1])
            if self.solveR(i,j-1):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i][j-1],True)
        
        # move bot
        if(
            j < self.numRows - 1
            and not self._cells[i][j].hasBotWall
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].drawMove(self._cells[i][j+1])
            if self.solveR(i,j+1):
                return True
            else:
                self._cells[i][j].drawMove(self._cells[i][j+1],True)
        
        return False

    def solve(self):
        return self.solveR(0,0)