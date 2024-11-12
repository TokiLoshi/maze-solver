from graphics import Window
from maze import Maze
import sys

def main(): 
  print("Let's build a maze solver with Tkinter")
  num_rows = 6 
  num_cols = 8 
  margin = 50 
  screen_x = 800
  screen_y = 600 
  cell_size_x = (screen_x - 2 * margin) / num_cols
  cell_size_y = (screen_y - 2 * margin) / num_rows
  sys.setrecursionlimit(1000)
  window = Window(screen_x, screen_y)
  maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window, 10)
  print("Commence solving!")
  solved = maze.solve()
  if solved:
    print("Congratulations, you solved the maze")
  else:
    print("Better luck next time")
  window.wait_for_close()
  


main()