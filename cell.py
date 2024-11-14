from graphics import Line, Point 

class Cell:
  def __init__(self, win=None):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self._win = win
    self._visited = False

  """Corners
    Top-left corner (x1, y1)
    Top right corner (x2, y1)
    Bottom left = (x1, y2)
    Bottom right = (x2, y2)
  """
  
  def draw(self, x1, y1, x2, y2):
    if self._win is None: 
      return 
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1  
    self._y2 = y2
    
    # Left wall is x1, y1 to x1, y2 
    if self.has_left_wall:
      line = Line(Point(x1, y1), Point(x1, y2))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1, y1), Point(x1, y2))
      self._win.draw_line(line, "black")

    # Top wall is x1, y2 to x2, y2
    if self.has_top_wall:
      line = Line(Point(x1, y1), Point(x2, y1))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1, y1), Point(x2, y1))
      self._win.draw_line(line, "black")

    # Right wall is x2, y2 to x1, y1 
    if self.has_right_wall:
      line = Line(Point(x2, y1), Point(x2, y2))
      self._win.draw_line(line)
    else: 
      line = Line(Point(x2, y1), Point(x2, y2))
      self._win.draw_line(line, "black")
    
    # Bootm wall is x1, y1 to x2, y1 
    if self.has_bottom_wall:
      line = Line(Point(x1, y2), Point(x2, y2))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1, y2), Point(x2, y2))
      self._win.draw_line(line, "black")
    
    
  def draw_move(self, to_cell, undo=False):
    half_length = abs(self._x2 - self._x1) // 2 
    x_center = half_length + self._x1 
    y_center = half_length + self._y1 

    half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
    x_center2 = half_length2 + to_cell._x1 
    y_center2 = half_length2 + to_cell._y1 
    
    fill_color = "white"
    if undo: 
      fill_color = "grey"
    line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
    self._win.draw_line(line, fill_color)

