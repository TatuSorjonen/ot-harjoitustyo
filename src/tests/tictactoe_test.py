import unittest
from tictactoeboard import TicTacToeBoard
from tictactoe import TicTacToe
from board import Board
from board import Result


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.my_tictactoe = TicTacToe(1000, 5)

    """
    def test_constructor_is_working(self):
        self.assertTrue(self.my_tictactoe.block_size >= 50, "Too many squares")
        self.assertTrue(self.my_tictactoe.block_size < self.my_tictactoe.grid_size /
                        self.my_tictactoe.num_for_win, "Too little squares")
                        
    #def test_how_many_characters_cant_go_higher_than_num_squares(self):
        #self.grid.run()
        #self.assertTrue(self.grid.how_many_characters <= (self.grid.num_squares * self.grid.num_squares))
    """
    
    #def test_run_works(self):
        #self.my_tictactoe.run()
        
    def test_draw_xo(self):
        self.assertEqual(self.my_tictactoe.board.result, Result.ONGOING)
        self.assertEqual(self.my_tictactoe.board.whose_turn, 1)
        self.my_tictactoe.draw_xo(0, 0)
        self.assertEqual(self.my_tictactoe.board.whose_turn, 2)
        self.assertEqual(self.my_tictactoe.board.result, Result.ONGOING)
        self.my_tictactoe.draw_xo(0, 0)
        self.assertEqual(self.my_tictactoe.board.whose_turn, 2)
        self.assertEqual(self.my_tictactoe.board.result, Result.ONGOING)
        self.my_tictactoe.draw_xo(self.my_tictactoe.grid_size - 1, self.my_tictactoe.grid_size - 1)
        self.assertEqual(self.my_tictactoe.board.whose_turn, 1)
        self.assertEqual(self.my_tictactoe.board.result, Result.ONGOING)
        
class TestTicTacToeBoard(unittest.TestCase):

    def setUp(self):
        self.my_tictactoe_board = TicTacToeBoard(5)
        
    def test_constructor_is_working(self):
        self.assertEqual(self.my_tictactoe_board.num_squares, 5)
        boolean = False
        if all('-' in x for x in self.my_tictactoe_board.board):
            boolean = True
        self.assertEqual(boolean, True)
        
    def test_adding_x_and_o(self):
    
        # Add first x to empty square
        self.my_tictactoe_board.add_x(0,0)
        self.assertEqual(sum(x.count("x") for x in self.my_tictactoe_board.board), 1)
        self.assertEqual(sum(x.count("-") for x in self.my_tictactoe_board.board), (self.my_tictactoe_board.num_squares ** 2) - 1)
    
        # Test to add x into occupied square
        self.my_tictactoe_board.add_x(0,0)
        self.assertEqual(sum(x.count("x") for x in self.my_tictactoe_board.board), 1)
        self.assertEqual(sum(x.count("-") for x in self.my_tictactoe_board.board), (self.my_tictactoe_board.num_squares ** 2) - 1)
        
        # Add o to an empty square
        self.my_tictactoe_board.add_o(0,1)
        self.assertEqual(sum(x.count("o") for x in self.my_tictactoe_board.board), 1)
        self.assertEqual(sum(x.count("-") for x in self.my_tictactoe_board.board), (self.my_tictactoe_board.num_squares ** 2) - 2)
        
        # Add o to same square than x
        self.my_tictactoe_board.add_o(0,0)
        self.assertEqual(sum(x.count("o") for x in self.my_tictactoe_board.board), 1)
        self.assertEqual(sum(x.count("-") for x in self.my_tictactoe_board.board), (self.my_tictactoe_board.num_squares ** 2) - 2)
        
    def test_if_taken(self):
        self.my_tictactoe_board.add_x(0,0)
        self.assertTrue(self.my_tictactoe_board.is_taken(0,0))
        
    def test_set_winner_right(self):
        self.my_tictactoe_board.set_winner('x')
        self.assertEqual(self.my_tictactoe_board.result, Result.FIRST_WIN)
        self.my_tictactoe_board.set_winner('o')
        self.assertEqual(self.my_tictactoe_board.result, Result.SECOND_WIN)
        
    def test_check_draw(self):
        self.my_tictactoe_board.add_x(0,0)
        self.my_tictactoe_board.add_o(0,1)
        self.my_tictactoe_board.add_o(0,2)
        self.my_tictactoe_board.add_o(0,3)
        self.my_tictactoe_board.add_x(0,4)
        self.my_tictactoe_board.add_x(1,0)
        self.my_tictactoe_board.add_o(1,1)
        self.my_tictactoe_board.add_x(1,2)
        self.my_tictactoe_board.add_x(1,3)
        self.my_tictactoe_board.add_o(1,4)
        self.my_tictactoe_board.add_o(2,0)
        self.my_tictactoe_board.add_x(2,1)
        self.my_tictactoe_board.add_o(2,2)
        self.my_tictactoe_board.add_x(2,3)
        self.my_tictactoe_board.add_o(2,4)
        self.my_tictactoe_board.add_x(3,0)
        self.my_tictactoe_board.add_x(3,1)
        self.my_tictactoe_board.add_o(3,2)
        self.my_tictactoe_board.add_o(3,3)
        self.my_tictactoe_board.add_x(3,4)
        self.my_tictactoe_board.add_x(4,0)
        self.my_tictactoe_board.add_o(4,1)
        self.my_tictactoe_board.add_o(4,2)
        self.my_tictactoe_board.add_x(4,3)
        self.my_tictactoe_board.add_x(4,4)
        self.my_tictactoe_board.check_draw()
        self.assertEqual(self.my_tictactoe_board.result, Result.DRAW)
        
    def test_check_situation(self):
        self.my_tictactoe_board.add_x(0,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(0,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(0,2)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,2)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(0,3)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.FIRST_WIN)
