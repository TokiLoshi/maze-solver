from graphics import Line, Point 

class Cell:
  def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, x2, y1, y2, win):
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2 
    self._win = win 

  """Corners
    Top-left corner (x1, y1)
    Top right corner (x2, y1)
    Bottom left = (x1, y2)
    Bottom right = (x2, y2)
  """
  def draw(self, canvas):
    if self.has_left_wall:
      canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)
    if self.has_right_wall:
      canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
    if self.has_top_wall:
      canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
    if self.has_bottom_wall:
      canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)
    
  def draw_move(self, to_cell, canvas, undo=False):
    fill_color = "gray"
    if undo: 
      fill_color = "red"
    from_midpoint_x = (self._x1 + self._x2) / 2
    from_midpoint_y = (self._y1 + self._y2) / 2 
    to_midpoint_x = (to_cell._x1 + to_cell._x2) / 2
    to_midpoint_y = (to_cell._x2 + to_cell._y2) / 2
    canvas.create_line(from_midpoint_x, from_midpoint_y, to_midpoint_x, to_midpoint_y, fill=fill_color, width=2)