from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):    
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)

        self.__canvas.pack(fill="both", expand=1)

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

    def draw_line(self, line):
        line.draw(self.__canvas, fill_color="black")


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

class Cell():
    def __init__(self, _x1, _y1, _x2, _y2, _win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = _x1
        self._y1 = _y1
        self._x2 = _x2
        self._y2 = _y2
        self._win = _win

    def draw(self):
        lines = []
        if self.has_top_wall:
            lines.append(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_right_wall:
            lines.append(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            lines.append(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        if self.has_left_wall:
            lines.append(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
            

        for line in lines:
            self._win.draw_line(line)