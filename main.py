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
    draw_cells(2, 100, win, 50)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()