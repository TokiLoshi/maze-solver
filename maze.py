from cell import Cell 
import time 

class Maze():
  #           self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, x2, y1, y2, win
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
    self.x1 = x1 
    self.y1 = y1 
    self.num_rows = num_rows 
    self.num_cols = num_cols 
    self.cell_size_x = cell_size_x 
    self.cell_size_y = cell_size_y 
    self.win = win 

  def _create_cells(self):
    self.cells = []
    for i in range(self.num_cols):
      col = []
      for j in range(self.num_rows):
        new_cell = Cell(True, True, True, True, self.x1, self.x1, self.y1, self.y1, self.win)
        col.append(new_cell)
      self._cells.append(col)

    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self._draw_cell(i, j)


  def _draw_cell(self, i, j):
    # calculate top-left corner (x1, y1)
    x1 = self.x1 + (i * self.cell_size_x)
    y1 = self.y1 + (j * self.cell_size_y)

    # calculate bottom right corner (x2, y2)
    x2 = self.x2 + self.cell_size_x
    y2 = self.y2 + self.cell_size_y

    # Update the coordinates
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()


  def _animate(self):
    self.win.redraw()
    time.sleep(0.05)
