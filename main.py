from window import Window, Point, Line

def main():
    print("Main Function Running...")

    win = Window(800, 600)
    
    line_1 = Line(Point(0, 0), Point(100, 100))

    win.draw_line(line_1, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()