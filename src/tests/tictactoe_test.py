import unittest
from unittest.mock import patch
from tictactoeboard import TicTacToeBoard
from tictactoe import TicTacToe
from tictactoeboard import Result
import tkinter as tk
from tkinter import *
from startmenu import StartMenu

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.my_tictactoe = TicTacToe()


    def test_constructor_is_working(self):
        self.assertEqual(self.my_tictactoe.tictactoeboard, None)
        self.assertEqual(self.my_tictactoe.screen, None)
        self.assertEqual(self.my_tictactoe.x_image, None)
        self.assertEqual(self.my_tictactoe.o_image, None)
        self.assertEqual(self.my_tictactoe.square_size, 0)
        self.assertEqual(self.my_tictactoe.grid_size, 800)
        self.assertEqual(self.my_tictactoe.result_text, '')

    def test_players_name_right(self):
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(5, '', '')
        names_ok = self.my_tictactoe.players_name_ok(max_size = 10)
        self.assertFalse(names_ok)
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(5, 'Test', 'Test2')
        names_ok = self.my_tictactoe.players_name_ok(max_size = 10)
        self.assertTrue(names_ok)
        self.my_tictactoe.tictactoeboard.player2 = 'Test2Test2Test2Test2'
        names_ok = self.my_tictactoe.players_name_ok(max_size = 10)
        self.assertFalse(names_ok)

    def test_who_wins_works(self):
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(5, 'Test', 'Test2') 
        self.my_tictactoe.set_game()
        self.my_tictactoe.tictactoeboard.result = Result.FIRST_WIN
        self.my_tictactoe.set_result()
        self.assertEqual(self.my_tictactoe.result_text, f"{self.my_tictactoe.tictactoeboard.player1} voittaa")
        self.my_tictactoe.tictactoeboard.result = Result.SECOND_WIN
        self.my_tictactoe.set_result()
        self.assertEqual(self.my_tictactoe.result_text, f"{self.my_tictactoe.tictactoeboard.player2} voittaa")
        self.my_tictactoe.tictactoeboard.result = Result.DRAW
        self.my_tictactoe.set_result()
        self.assertEqual(self.my_tictactoe.result_text, 'Tasapeli')

    def test_draw_right_player(self):
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(5, 'Test', 'Test2') 
        self.my_tictactoe.set_game()
        self.assertEqual(self.my_tictactoe.whose_turn, f"Vuoro: {self.my_tictactoe.tictactoeboard.player1}")
        self.my_tictactoe.tictactoeboard.whose_turn = 2
        self.my_tictactoe.draw_status()
        self.assertEqual(self.my_tictactoe.whose_turn, f"Vuoro: {self.my_tictactoe.tictactoeboard.player2}")

    def test_draw_xo(self):
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(5, 'Test', 'Test2')
        self.my_tictactoe.set_game()
        self.assertEqual(self.my_tictactoe.tictactoeboard.result, Result.ONGOING)
        self.assertEqual(self.my_tictactoe.tictactoeboard.whose_turn, 1)
        self.my_tictactoe.set_xo(0, 0)
        self.assertEqual(self.my_tictactoe.tictactoeboard.whose_turn, 2)
        self.assertEqual(self.my_tictactoe.tictactoeboard.result, Result.ONGOING)
        self.my_tictactoe.set_xo(0, 0)
        self.assertEqual(self.my_tictactoe.tictactoeboard.whose_turn, 2)
        self.assertEqual(self.my_tictactoe.tictactoeboard.result, Result.ONGOING)
        self.my_tictactoe.set_xo(self.my_tictactoe.grid_size - 1, self.my_tictactoe.grid_size - 1)
        self.assertEqual(self.my_tictactoe.tictactoeboard.whose_turn, 1)
        self.assertEqual(self.my_tictactoe.tictactoeboard.result, Result.ONGOING)

    def test_variables_after_set_num_squares(self):
        self.my_tictactoe.tictactoeboard = TicTacToeBoard(0, 'Test', 'Test2')
        self.assertEqual(self.my_tictactoe.tictactoeboard.num_squares, 0)
        self.assertTrue(self.my_tictactoe.screen == None)
        self.assertTrue(self.my_tictactoe.x_image == None)
        self.assertTrue(self.my_tictactoe.o_image == None)
        self.assertTrue(self.my_tictactoe.tictactoeboard != None)
        self.assertTrue(self.my_tictactoe.square_size == 0)
        self.assertTrue(self.my_tictactoe.grid_size == 800)
        self.my_tictactoe.tictactoeboard.num_squares = 5
        self.my_tictactoe.set_game()
        self.assertTrue(self.my_tictactoe.tictactoeboard.num_squares <= 30 and self.my_tictactoe.tictactoeboard.num_squares >= 5)
        self.assertTrue(self.my_tictactoe.screen != None)
        self.assertTrue(self.my_tictactoe.x_image != None)
        self.assertTrue(self.my_tictactoe.o_image != None)
        self.assertTrue(self.my_tictactoe.tictactoeboard != None)
        self.assertTrue(self.my_tictactoe.square_size == int(self.my_tictactoe.grid_size/self.my_tictactoe.tictactoeboard.num_squares))
        self.assertTrue(self.my_tictactoe.grid_size == self.my_tictactoe.grid_size - (self.my_tictactoe.grid_size % self.my_tictactoe.tictactoeboard.num_squares))
        
    def test_quit_button(self):
        self.my_tictactoe.check_button_pressed(self.my_tictactoe.grid_size - 1, self.my_tictactoe.grid_size + self.my_tictactoe.bottom_height - 1)
        self.assertEqual(self.my_tictactoe.running, False)

class TestStartMenu(unittest.TestCase):

    def setUp(self):
        self.start_menu = StartMenu('Tasapeli')

    def test_constructor(self):
        self.assertEqual(self.start_menu.num_squares, 0)
        self.assertEqual(self.start_menu.player1, '')
        self.assertEqual(self.start_menu.player2, '')
        self.assertEqual(self.start_menu.name_max_size, 10)
        self.assertEqual(self.start_menu.window_width, 600)
        self.assertEqual(self.start_menu.window_height, 450)
        self.assertEqual(self.start_menu.previous_result, 'Tasapeli')


    def test_set_num_squares_is_working(self):
        slider = Scale(self.start_menu.root, from_=5, to=30, orient=HORIZONTAL, sliderlength=200, length=500, width=30)
        slider.pack()
        player1_name = Entry(width = 30)
        player1_name.pack()
        player2_name = Entry(width = 30)
        player2_name.pack()
        self.start_menu.player1 = 'Testi'
        self.start_menu.player2 = 'Testi2'
        self.start_menu.set_num_squares(slider, player1_name, player2_name)
        self.assertTrue(self.start_menu.num_squares == 5)
        self.assertEqual(self.start_menu.player1, '')
        self.assertEqual(self.start_menu.player2, '')
        
    def test_set_window(self):
        self.start_menu.set_window()
        self.assertEqual(self.start_menu.root.title(), 'Aloita uusi ristinolla-peli')
        
    def test_set_players(self):
        player1, player2 = self.start_menu.set_players()
        self.assertEqual(player1.get(), '')
        self.assertEqual(player2.get(), '')
        

class TestTicTacToeBoard(unittest.TestCase):

    def setUp(self):
        self.my_tictactoe_board = TicTacToeBoard(5, '', '')

    def test_constructor_is_working(self):
        self.assertEqual(self.my_tictactoe_board.num_squares, 5)
        boolean = False
        if all('-' in x for x in self.my_tictactoe_board.board):
            boolean = True
        self.assertEqual(boolean, True)
        self.assertEqual(self.my_tictactoe_board.whose_turn, 1)
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)

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

    def test_check_situation_row(self):
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

    def test_check_situation_col(self):
        self.my_tictactoe_board.add_x(0,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(0,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(1,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(2,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(2,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(3,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.FIRST_WIN)

    def test_check_situation_diagonal(self):
        self.my_tictactoe_board.add_x(0,0)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(0,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(1,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(2,2)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(2,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(3,3)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.FIRST_WIN)

    def test_check_situation_diagonal_other_way(self):
        self.my_tictactoe_board.add_x(0,4)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(0,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(1,3)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(1,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(2,2)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_o(2,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.ONGOING)
        self.my_tictactoe_board.add_x(3,1)
        self.my_tictactoe_board.check_situation()
        self.assertEqual(self.my_tictactoe_board.result, Result.FIRST_WIN)
