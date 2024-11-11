import unittest 
from maze import Maze 

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10 
    num_cols2 = 14 
    num_rows2 = 12
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    m2 = Maze(0, 0, num_rows2, num_cols2, 10, 10)
    self.assertEqual(
      len(m1._cells),
      num_cols,
    )
    self.assertEqual(
      len(m1._cells[0]),
      num_rows,
    )
    self.assertEqual(
      len(m2._cells),
      num_cols2
    )
    self.assertEqual(
      len(m2._cells[0]),
      num_rows2
    )
  def test_entrance_and_exit(self):
    num_cols = 12 
    num_rows = 10 
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    m1_entrance = m1._cells[0][0]
    m1_exit = m1._cells[num_cols - 1][num_rows - 1]
    self.assertEqual(
      m1_entrance.has_top_wall, False
    )
    self.assertEqual(
      m1_exit.has_bottom_wall, False
    )
    

if __name__ == "__main__":
  unittest.main()
