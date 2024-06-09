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

def main():
    win = Window(800,600)
    win.waitForClose()

if __name__ == "__main__":
    main()