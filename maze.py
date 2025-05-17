from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        for col in self._cells:
            for cell in col:
                print(cell._visited)
        self._solve()


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

    def _draw_cell(self, i, j, speed=0.01):
        if self._win == None:
            return

        x1 = self.x1 + (self.cell_size_x * i)
        y1 = self.y1 + (self.cell_size_y * j)
        x2 = self.x1 + (self.cell_size_x * (i + 1))
        y2 = self.y1 + (self.cell_size_y * (j + 1))

        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate(speed)

    def _break_walls_r(self, i, j, seed=None): 

        current_cell = self._cells[i][j]
        current_cell._visited = True

        while True:
            possible_coordinates = [["top neighbor", i, j - 1], ["bottom neighbor", i, j + 1], ["left neighbor", i - 1, j], ["right neighbor", i + 1, j]]

            to_visit = []

            for coord in possible_coordinates:
                _i = coord[1]
                _j = coord[2]

                if _i == i: 
                    if 0 <= _j < self.num_rows and self._cells[_i][_j]._visited == False:
                        to_visit.append(coord)
                else:
                    if 0 <= _i < self.num_cols and self._cells[_i][_j]._visited == False:
                        to_visit.append(coord)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                break
            else:   
                wall_to_break = to_visit[random.randint(0, len(to_visit) - 1)]

                neighbor = self._cells[wall_to_break[1]][wall_to_break[2]]

                match wall_to_break[0]:
                    case "top neighbor":
                        current_cell.has_top_wall = False

                        neighbor.has_bottom_wall = False

                    case "right neighbor":
                        current_cell.has_right_wall = False

                        neighbor.has_left_wall = False

                    case "bottom neighbor":
                        current_cell.has_bottom_wall = False

                        neighbor.has_top_wall = False

                    case "left neighbor":
                        current_cell.has_left_wall = False

                        neighbor.has_right_wall = False

                self._break_walls_r(wall_to_break[1], wall_to_break[2])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    def _solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):

        self._animate(0.02)

        print(i, j)

        current_cell = self._cells[i][j]

        current_cell._visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            print("solved")
            return True

        if current_cell.has_top_wall == False and i != 0 and j != 0 and self._cells[i][j - 1]._visited == False:
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1) == True:
                return True
            else:
                current_cell.draw_move(self._cells[i][j - 1], True)
        if current_cell.has_right_wall == False and self._cells[i + 1][j]._visited == False:
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j) == True:
                return True
            else:
                current_cell.draw_move(self._cells[i + 1][j], True)
        if current_cell.has_bottom_wall == False and self._cells[i][j + 1]._visited == False:
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1) == True:
                return True
            else:
                current_cell.draw_move(self._cells[i][j + 1], True)
        if current_cell.has_left_wall == False and self._cells[i - 1][j]._visited == False:
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j) == True:
                return True
            else:
                current_cell.draw_move(self._cells[i - 1][j], True)
                
        return False

        possible_coords = []

        # if current_cell.has_top_wall == False and i != 0 and j != 0:
        #     possible_coords.append([i, j - 1])
        # if current_cell.has_right_wall == False:
        #     possible_coords.append([i + 1, j])
        # if current_cell.has_bottom_wall == False:
        #     possible_coords.append([i, j + 1])
        # if current_cell.has_left_wall == False:
        #     possible_coords.append([i - 1, j])

        
 

    
    def _animate(self, speed):
        if self._win == None:
            return
        
        self._win.redraw()
        time.sleep(speed)

    def __eq__(self, other_node):
        is_equal = self.x1 == other_node.x1 and self.y1 == other_node.y1 and self.num_rows == other_node.num_rows and self.num_cols == other_node.num_cols and self.cell_size_x == other_node.cell_size_x and self.cell_size_y == other_node.cell_size_y and self.cells == other_node.cells

        return is_equal
