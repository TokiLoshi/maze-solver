from graphics import Window, Line, Point, Cell

def main(): 
  print("Let's build a maze solver with Tkinter")
  window = Window(800, 600)
  line = Line(Point(50, 50), Point(100, 100))
  window.draw_line(line, "green") 
  first_cell = Cell(True, True, True, True, 40, 100, 80, 200, window)
  second_cell = Cell(True, True, True, True, 100, 200, 400, 500, window)
  canvas = window.get_canvas()
  first_cell.draw(canvas)
  second_cell.draw(canvas)
  move = first_cell.draw_move(second_cell, canvas, undo=False)
  window.wait_for_close()





main()