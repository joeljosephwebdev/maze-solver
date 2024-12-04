from graphics import Window, Point, Line

def main():
    win = Window(800, 600)

    start_point = Point(100, 100)
    end_point = Point(100, 200)
    line = Line(start_point, end_point)
    win.draw_line(line, )

    start_point = Point(100, 200)
    end_point = Point(200, 200)
    line = Line(start_point, end_point)
    win.draw_line(line, "red")

    start_point = Point(200, 200)
    end_point = Point(200, 100)
    line = Line(start_point, end_point)
    win.draw_line(line, "blue")

    start_point = Point(200, 100)
    end_point = Point(100, 100)
    line = Line(start_point, end_point)
    win.draw_line(line, "green")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()