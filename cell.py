from graphics import Point

class Cell:
    def __init__(self,x1,y1,x2,y2,win, visited=False):
        self.hasLeftWall = True
        self.hasRightWall = True
        self.hasTopWall = True
        self.hasBotWall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = visited
    
    def draw(self,x1,y1,x2,y2,lineColor="black"):
        if self.hasTopWall:
            self._win.canvasWidget.create_line(
                x1,y1,
                x2,y1,
                fill=lineColor)
        else:
            self._win.canvasWidget.create_line(
                x1,y1,
                x2,y1,
                fill="white")

        if self.hasLeftWall:
            self._win.canvasWidget.create_line(
                x1,y1,
                x1,y2,
                fill=lineColor)       
        else:
            self._win.canvasWidget.create_line(
                x1,y1,
                x1,y2,
                fill="white")    
        
        if self.hasRightWall:
            self._win.canvasWidget.create_line(
                x2,y1,
                x2,y2,
                fill=lineColor)
        else:
            self._win.canvasWidget.create_line(
                x2,y1,
                x2,y2,
                fill="white")
        
        if self.hasBotWall:
            self._win.canvasWidget.create_line(
                x1,y2,
                x2,y2,
                fill=lineColor)
        else:
            self._win.canvasWidget.create_line(
                x1,y2,
                x2,y2,
                fill="white")

    def drawMove(self, toCell, undo=False):
        center = Point((self._x1 + self._x2)/2,(self._y1 + self._y2)/2)
        toCenter = Point((toCell._x1 + toCell._x2)/2,(toCell._y1 + toCell._y2)/2)
        color = "red"
        if undo:
            color = "gray"
            
        self._win.canvasWidget.create_line(
            center.x,center.y,
            toCenter.x,toCenter.y,
            fill=color
        )