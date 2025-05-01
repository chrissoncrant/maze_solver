from graphics import Point, Line

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
        self._center_x = self._x1 + (self._x2 - self._x1) / 2
        self._center_y = self._y1 + (self._y2 - self._y1) / 2
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

    def draw_move(self, to_cell, undo=False):
        path_line = Line(Point(self._center_x, self._center_y), Point(to_cell._center_x, to_cell._center_y))

        if undo:
            self._win.draw_line(path_line, "red")
        else:
            self._win.draw_line(path_line, "gray")