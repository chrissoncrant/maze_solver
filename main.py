from window import Window, Point, Line, Cell
from utilities import draw_cells

import random

def main():
    print("Main Function Running...")

    win = Window(800, 600)


    # DRAW LINE TEST
    # line_1 = Line(Point(0, 0), Point(100, 100))

    # win.draw_line(line_1, "black")

    # DRAW CELL TEST
    # draw_cells(2, 100, win, 50)
    c_1 = Cell(50, 50, 100, 100, win)
    c_2 = Cell(100, 100, 150, 150, win)

    c_1.draw()
    c_2.draw()

    c_1.draw_move(c_2, True)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()