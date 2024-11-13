from cell import Cell 
import time 
import random

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    self._cells = []
    self._x1 = x1 
    self._y1 = y1 
    self._num_rows = num_rows 
    self._num_cols = num_cols 
    self._cell_size_x = cell_size_x 
    self._cell_size_y = cell_size_y 
    self._win = win 
    self._seed = seed
    if self._seed is None:
      self._seed = random.seed()
    
    
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()

  def _create_cells(self):
    for i in range(self._num_cols):
      col_cells = []
      for j in range(self._num_rows):
        new_cell = Cell(self._win)
        col_cells.append(new_cell)
      self._cells.append(col_cells)

    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i, j)


  def _draw_cell(self, i, j):
    if self._win is None:
      return
    x1 = self._x1 + i * self._cell_size_x
    y1 = self._y1 + j * self._cell_size_y
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y

    # Update the coordinates
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()
  

  def _animate(self):
    if self._win is None: 
      return
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
      self._cells[0][0].has_top_wall = False
      self._draw_cell(0, 0)
      self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
      self._draw_cell(self._num_cols - 1, self._num_rows - 1)
 
 
  def _break_walls_r(self, i, j):
    # Mark the current cell as visited 
    self._cells[i][j]._visited = True 
    self._draw_cell(i, j)
    # start an infinite loop
    while True:
      # create a new empty list to hold i and j values to visit 
      cells_to_visit = [] 
      
      # Check the cells that are directly adjacent to current cell 
  
      # Moving down 
      if j  < self._num_rows - 1:
        bottom_cell = self._cells[i][j + 1]
        if not bottom_cell._visited: 
          cells_to_visit.append((i, j + 1))
      
      # Moving up 
      if j > 0:
          top_cell = self._cells[i][j - 1]
          if not top_cell._visited: 
            cells_to_visit.append((i, j - 1))
      
      # Moving right
      if i < self._num_cols - 1:
          right_cell = self._cells[i + 1][j]
          if not right_cell._visited:
            cells_to_visit.append((i + 1, j))
      
      # Moving left 
      if i > 0:
          left_cell = self._cells[i - 1][j]
          if not left_cell._visited:
            cells_to_visit.append((i - 1, j))
      
      # if there are zero directions you can go to from current cell draw the current cell
      if not len(cells_to_visit):
        self._draw_cell(i, j)
        # return to break out of the loop
        return 
    
      # pick a random direction 
      random_index = random.randrange(0, len(cells_to_visit))
      next_cell = cells_to_visit[random_index]
      
      # knock down wall between current cell and chosen cell 
      next_i = next_cell[0]
      next_j = next_cell[1]
      
      # move up 
      if next_j == j - 1:
        # break this cells top wall 
        self._cells[i][j].has_top_wall = False 
        # break next_cells bottom wall  
        self._cells[next_i][next_j].has_bottom_wall = False 
      
      # move down 
      elif next_j == j + 1: 
        # break this cells bottom wall
        self._cells[i][j].has_bottom_wall = False
        # break next cells top wall 
        self._cells[next_i][next_j].has_top_wall = False 

      # move right 
      elif next_i == i + 1:
        # break this cells right wall 
        self._cells[i][j].has_right_wall = False 
        # break next cells left wall 
        self._cells[next_i][next_j].has_left_wall = False

      # move left 
      elif next_i == i -1:
        # break this cells left wall 
        self._cells[i][j].has_left_wall = False
        # break next cell's right wall
        self._cells[next_i][next_j].has_right_wall = False 
      self._break_walls_r(next_i, next_j)

  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
        cell._visited = False

  def _solve_r(self, i, j):
    
    # Call animate method
    self._animate()
    
    # Mark current cell as visited 
    self._cells[i][j]._visited = True 

    # if end of cell (goal) return True
    if i == self._num_cols - 1 and j == self._num_rows - 1: 
      return True 
    
    # move down if no wall and hasn't been visited
    if (j < self._num_rows - 1 and not self._cells[i][j + 1]._visited and not self._cells[i][j].has_bottom_wall):
        self._cells[i][j].draw_move(self._cells[i][j + 1])
        if self._solve_r(i, j + 1):
          return True
        else:
          self._cells[i][j].draw_move(self._cells[i][j + 1], True)
      
    # move up if no wall and hasn't been visited 
    if (j > 0 and not self._cells[i][j - 1]._visited and not self._cells[i][j].has_top_wall):
        self._cells[i][j].draw_move(self._cells[i][j - 1])
        if self._solve_r(i, j - 1):
          return True
        else:
          self._cells[i][j].draw_move(self._cells[i][j - 1], True)
    
    # move left if no wall and it hasn't been visited 
    if (i > 0 and not self._cells[i - 1][j]._visited and not self._cells[i][j].has_left_wall):
        self._cells[i][j].draw_move(self._cells[i - 1][j])
        if self._solve_r(i - 1, j):
          return True
        else:
          self._cells[i][j].draw_move(self._cells[i - 1][j], True)
    
    # move right if no wall and hasn't been visited 
    if (i < self._num_cols - 1 and not self._cells[i + 1][j]._visited and not self._cells[i][j].has_right_wall):
        self._cells[i][j].draw_move(self._cells[i + 1][j])
        if self._solve_r(i + 1, j):
          return True
        else:
          self._cells[i][j].draw_move(self._cells[i + 1][j], True)
    
    # we went the wrong way return false
    return False 

  def solve(self):
    return self._solve_r(0, 0)
     
      
      
     
      
    