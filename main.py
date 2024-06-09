from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.rootWidget = Tk()
        self.rootWidget.title("Maze Solver")
        self.canvasWidget = Canvas(self.rootWidget,width=width,height=height)
        self.canvasWidget.pack()
        self.isRunning = False
        self.rootWidget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.rootWidget.update_idletasks()
        self.rootWidget.update()

    def waitForClose(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()
    
    def close(self):
        self.isRunning = False
    
    def drawLine(self,line,fillColor):
        line.draw(self.canvasWidget,fillColor)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas,lineColor="black"):
        canvas.create_line(
            self.point1.x,self.point1.y,
            self.point2.x,self.point2.y
            ,fill=lineColor,
            width = 2)

class Cell:
    def __init__(self,x1,y1,x2,y2,win):
        self.hasLeftWall = True
        self.hasRightWall = True
        self.hasTopWall = True
        self.hasBotWall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
    
    def draw(self,lineColor="black"):
        if self.hasTopWall:
            self._win.canvasWidget.create_line(
                self._x1,self._y1,
                self._x2,self._y1,
                fill=lineColor)

        if self.hasLeftWall:
            self._win.canvasWidget.create_line(
                self._x1,self._y1,
                self._x1,self._y2,
                fill=lineColor)       

        if self.hasRightWall:
            self._win.canvasWidget.create_line(
                self._x2,self._y1,
                self._x2,self._y2,
                fill=lineColor)

        if self.hasBotWall:
            self._win.canvasWidget.create_line(
                self._x1,self._y2,
                self._x2,self._y2,
                fill=lineColor)

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

def main():
    win = Window(800,600)
    point1=Point(10,10)
    point2=Point(100,100)
    cell1=Cell(point1.x,point1.y,point2.x,point2.y,win)
    cell1.draw()
    win.waitForClose()

if __name__ == "__main__":
    main()