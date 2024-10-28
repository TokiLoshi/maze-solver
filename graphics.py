
from tkinter import Tk, BOTH, Canvas

class Window: 
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.title("Maze Solver")
    self._canvas = Canvas(self.__root, bg="white", width=width, height=height)
    self._canvas.pack(fill=BOTH, expand=1)
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)
  
  def redraw(self):
    self.__root.update_idletasks()
    self.__root.update()

  def wait_for_close(self):
    self.__running = True 
    while self.__running:
      self.redraw()
    print("window closed")

  def close(self):
    self.__running = False

  def draw_line(self, line, fill_color="black"):
    line.draw(self._canvas, fill_color)

  def get_canvas(self):
    return self._canvas


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
  
  def draw(self, canvas, fill_color="black"):
    canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
  
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