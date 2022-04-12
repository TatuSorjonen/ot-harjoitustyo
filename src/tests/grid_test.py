import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(1000, 5, 4)

    #def test_grid_run(self):
        #self.grid.run()

    def test_constructor_is_working(self):
        self.assertTrue(self.grid.block_size >= 50, "Too many squares")
        self.assertTrue(self.grid.block_size < self.grid.grid_size /
                        self.grid.num_for_win, "Too little squares")
                        
    def test_how_many_characters_cant_go_higher_than_num_squares(self):
        self.grid.run()
        self.assertTrue(self.grid.how_many_characters <= (self.grid.num_squares * self.grid.num_squares))
