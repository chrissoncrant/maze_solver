from graphics import Window
from cell import Cell
from maze import Maze
from utilities import draw_cells

import random

def main():
    print("Main Function Running...")

    win = Window(1200, 600)


    # DRAW LINE TEST
    # line_1 = Line(Point(0, 0), Point(100, 100))

    # win.draw_line(line_1, "black")

    # DRAW CELL TEST
    # draw_cells(2, 100, win, 50)
    # c_1 = Cell(win)
    # c_2 = Cell(win)

    # c_1.draw(50, 50, 100, 100)
    # c_2.draw(100, 100, 150, 150)

    # c_1.draw_move(c_2, True)

    # DRAW MAZE TEST
    maze = Maze(50, 10, 3, 2, 50, 100, win)


    
    win.wait_for_close()

if __name__ == "__main__":
    main()