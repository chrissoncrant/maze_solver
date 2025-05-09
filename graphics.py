from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):    
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.geometry(f"{width}x{height}+100+200")

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)

        self.__canvas.pack(fill="both", expand=1, side="top")

        self.__window_running = False

    def redraw(self):
        
        self.__root.update_idletasks()

        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True

        while self.__window_running:
            self.redraw()

        print("window closed...")

    def close(self):
        self.__window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color=fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        if not isinstance(point_1, Point) or not isinstance(point_2, Point):
            raise ValueError("point needs to be of Point class")
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)

