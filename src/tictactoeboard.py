from board import Board
from board import Result

class TicTacToeBoard(Board):

    def __init__(self, num_squares):

        # Class variables
        super().__init__(num_squares)
        self.board = [['-' for i in range(num_squares)] for j in range(num_squares)]
        self.whose_turn = 1
        self.winner = 'Tasapeli'

    # Add x into table
    def add_x(self, x_square, y_square):

        # Check if square is not already taken and if not, switch turns
        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'x'
            self.whose_turn = 2

        # Check if someone wins
        self.check_situation()

        #Debug: remove later
        self.print_board()

    # Add o into table
    def add_o(self, x_square, y_square):

        # Check if square is not aldeary taken and if not, switch turns
        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'o'
            self.whose_turn = 1

        # Check if someone wins
        self.check_situation()

        #Debug: remove later
        self.print_board()

    # Function for, check if someone wins or not
    def check_situation(self):

        # Goes through the whole table
        for i in range(0, self.num_squares):
            for j in range(0, self.num_squares):
                #print(i, ",", j)

                # Check if square don't have xo and if there is one, calls check_winner function
                if self.board[i][j] == '-':
                    continue
                self.check_winner(i, j)

        # Calls check_draw() function for checking draw
        self.check_draw()

    # Check if someone wins
    def check_winner(self, i, j):

        # Check row
        if j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2]\
                                == self.board[i][j+3]:
                self.set_winner(self.board[i][j])

        # Check col
        if i + 3 < self.num_squares:
            if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j]\
                                == self.board[i+3][j]:
                self.set_winner(self.board[i][j])

        # Check diagonal up left to right down
        if i + 3 < self.num_squares and j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2]\
                                == self.board[i+3][j+3]:
                self.set_winner(self.board[i][j])

        # Check diagonal down left to right up
        if i - 3 >= 0 and j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2]\
                                == self.board[i-3][j+3]:
                self.set_winner(self.board[i][j])

    # Sets winner for game
    def set_winner(self, winner):

        # If x wins set x to win. Otherwise o wins
        if winner == 'x':
            self.result = Result.FIRST_WIN
            self.winner = 'X on voittaja'
        else:
            self.result = Result.SECOND_WIN
            self.winner = 'O on voittaja'

    def print_board(self):
        for i in self.board:
            print(i)
        print()

    # Check if square is taken and returns True or False
    def is_taken(self, y_square, x_square):
        return self.board[y_square][x_square] != '-'

    # Check if board is full and if it is, sets result to draw and game ends
    def check_draw(self):
        if not any('-' in x for x in self.board) and self.result == Result.ONGOING:
            self.result = Result.DRAW
