from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self._create_cells()
        self._break_entrance_and_exit()


    def _create_cells(self):

        for i in range(0, self.num_cols):
            col = []
        
            for j in range(0, self.num_rows):
                col.append(Cell(self._win))

            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        last_col_index = self.num_cols - 1
        last_row_index = self.num_rows - 1
        self._cells[last_col_index][last_row_index].has_bottom_wall = False
        self._draw_cell(last_col_index, last_row_index)




    def _draw_cell(self, i, j):
        if self._win == None:
            return

        x1 = self.x1 + (self.cell_size_x * i)
        y1 = self.y1 + (self.cell_size_y * j)
        x2 = self.x1 + (self.cell_size_x * (i + 1))
        y2 = self.y1 + (self.cell_size_y * (j + 1))

        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate()
        
    
    def _animate(self):
        if self._win == None:
            return
        
        self._win.redraw()
        time.sleep(0.3)

    def __eq__(self, other_node):
        is_equal = self.x1 == other_node.x1 and self.y1 == other_node.y1 and self.num_rows == other_node.num_rows and self.num_cols == other_node.num_cols and self.cell_size_x == other_node.cell_size_x and self.cell_size_y == other_node.cell_size_y and self.cells == other_node.cells

        return is_equal
