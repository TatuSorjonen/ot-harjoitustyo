import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(1000, 20, 4)
        
    def test_grid_run(self):
        self.grid.run()
        
    def test_constructor_is_working(self):
        self.assertTrue(self.grid.block_size >= 50, "Too many squares") 
        self.assertTrue(self.grid.block_size < self.grid.grid_size/self.grid.num_for_win, "Too little squares")
        
#if __name__ == "__main__":
    #unittest.main()
