from cell import Cell

def draw_cells(grid_size, cell_size, window, starting_point=0):
    col_count = 1
    row_count = 1
    cells = []

    while row_count <= grid_size:

        while col_count <= grid_size:
            x1 = starting_point + (cell_size * (col_count - 1))
            y1 = starting_point + (cell_size * (row_count - 1))
            x2 = starting_point + (cell_size * col_count)
            y2 = starting_point + (cell_size * row_count)

            cells.append(Cell(x1, y1, x2, y2, window))

            col_count += 1

        col_count = 1
        row_count += 1

    for i in range(len(cells)):
        cell = cells[i]
        if i == 1:
            cell.has_top_wall = False
        if i == 2:
            cell.has_left_wall = False
        cell.draw()