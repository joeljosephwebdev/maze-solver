from cell import Cell
from graphics import Window
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
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

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
