import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 12

        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)

        self.assertEqual(num_cols, len(m1._cells))
        self.assertEqual(num_rows, len(m1._cells[0]))

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 12

        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)

        first_cell = m1._cells[0][0]
        last_cell = m1._cells[-1][-1]

        self.assertEqual(False, first_cell.has_top_wall)
        self.assertEqual(False, last_cell.has_bottom_wall)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 3, 3, 10, 10)

        m1._reset_cells_visited()

        for col in m1._cells:
            for cell in col:
                self.assertEqual(False, cell._visited)



if __name__ == "__main__":
    unittest.main()