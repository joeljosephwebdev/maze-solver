from cell import Cell
from graphics import Window
import random
import time


class Maze:
    def __init__(
        self,
        x1 : int,
        y1 : int,
        num_rows : int,
        num_cols : int,
        cell_size_x : int,
        cell_size_y : int,
        win : Window = None,
        seed : int = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
      for col in range(self._num_cols):
          column = []
          self._cells.append(column)         # Add empty column to grid first
          for row in range(self._num_rows):
              new_cell = Cell(self._win)
              self._cells[col].append(new_cell)  # Add cell directly to self._cells
              self._draw_cell(col, row)          # Now we can draw it


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)
    
    def _break_entrance_and_exit(self):
        if random.choice([True, False]):
            self._cells[0][0].has_top_wall = False
        else:
            self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        if random.choice([True, False]):
          self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        else:
          self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(to_visit) < 1:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction = random.choice(to_visit)
            to_visit.remove(direction)

            # knock out walls between this cell and the next cell(s)
            # right
            if i < direction[0]:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._draw_cell(i, j)
            # left
            elif i > direction[0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                self._draw_cell(i, j)
            # up
            elif j > direction[1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._draw_cell(i, j)
            # down
            elif j < direction[1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._draw_cell(i, j)
            # recursively visit the next cell
            self._break_walls_r(direction[0], direction[1])
