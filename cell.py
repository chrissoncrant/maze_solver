from graphics import Point, Line

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, _x1, _y1, _x2, _y2):
        self._x1 = _x1
        self._y1 = _y1
        self._x2 = _x2
        self._y2 = _y2

        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")

        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")
            
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")

    def draw_move(self, to_cell, undo=False):
        self_center_x = self._x1 + (self._x2 - self._x1) / 2
        self_center_y = self._y1 + (self._y2 - self._y1) / 2
        other_center_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        other_center_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2

        path_line = Line(Point(self_center_x, self_center_y), Point(other_center_x, other_center_y))

        if undo:
            self._win.draw_line(path_line, "red")
        else:
            self._win.draw_line(path_line, "gray")