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