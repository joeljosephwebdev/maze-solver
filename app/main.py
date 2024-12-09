from graphics import Window
from maze import Maze
import sys
import time


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = 10

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    start = time.time()
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)
    end = time.time()
    print(f"maze created in {end - start}s")
    start = time.time()
    is_solvable = maze.solve()
    end = time.time()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print(f"maze solved! in {end - start}s")
    win.wait_for_close()

if __name__ == "__main__":
    main()