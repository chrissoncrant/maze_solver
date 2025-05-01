from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):

        for i in range(0, self.num_cols):
            col = []
        
            for j in range(0, self.num_rows):
                cell = self._draw_cell(i, j)

                col.append(cell)

            self._cells.append(col)

        for col in self._cells:
            for cell in col:
                cell.draw()
                self._animate()

    def _draw_cell(self, i, j):
        x1 = self.x1 + (self.cell_size_x * j)
        y1 = self.y1 + (self.cell_size_y * i)
        x2 = self.x1 + (self.cell_size_x * (j + 1))
        y2 = self.y1 + (self.cell_size_y * (i + 1))

        return Cell(x1, y1, x2, y2, self.win)
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.3)
