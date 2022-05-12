from board import Board
from board import Result

class TicTacToeBoard(Board):
    """Class that manages the properties of a tictactoe game. Inherits the class Board

    Attributes:
        Same as class Board and also
        board: set the board full '-' signs
        whose_turn: whose turn is it
        winner: Who wins at end
    """

    def __init__(self, num_squares):
        """Class contsructor which set all attributes at starting position

        Args:
            num_squares: how big is tictactoe board. Row and column

        """
        super().__init__(num_squares)
        self.board = [['-' for i in range(num_squares)] for j in range(num_squares)]
        self.whose_turn = 1

    # Add x into table
    def add_x(self, x_square, y_square):
        """Add x into table after checking if is taken or not. Then switch
        whose turn is it. At the end check if someone wins

        Args:
            x_square: What x square is it
            y_square: What y square is it

        """

        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'x'
            self.whose_turn = 2

        self.check_situation()

    def add_o(self, x_square, y_square):
        """Add o into table after checking if is taken or not. Then switch
        whose turn is it. At the end check if someone wins

        Args:
            x_square: What x square is it
            y_square: What y square is it

        """

        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'o'
            self.whose_turn = 1

        self.check_situation()

    def check_situation(self):
        """Goes through the entire board and check if there are x or o characters on the board.
        if so then call the check_winner function. And after all places are check, calls check_draw
        funcion
        """

        for i in range(0, self.num_squares):
            for j in range(0, self.num_squares):

                if self.board[i][j] == '-':
                    continue
                self.check_winner(i, j)

        self.check_draw()

    def check_winner(self, i, j):
        """Check if someone wins or not. First check row, then col. After that diagonals
        """

        if j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2]\
                                == self.board[i][j+3]:
                self.set_winner(self.board[i][j])

        if i + 3 < self.num_squares:
            if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j]\
                                == self.board[i+3][j]:
                self.set_winner(self.board[i][j])

        if i + 3 < self.num_squares and j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2]\
                                == self.board[i+3][j+3]:
                self.set_winner(self.board[i][j])

        if i - 3 >= 0 and j + 3 < self.num_squares:
            if self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2]\
                                == self.board[i-3][j+3]:
                self.set_winner(self.board[i][j])

    # Sets winner for game
    def set_winner(self, winner):
        """Set winner for game after checking if winner is x or not
        Args:
            winner: Who is winner
        """

        if winner == 'x':
            self.result = Result.FIRST_WIN
        else:
            self.result = Result.SECOND_WIN

    # Check if square is taken and returns True or False
    def is_taken(self, y_square, x_square):
        """Check if square is taken

        Args:
            x_square: What x square is it
            y_square: What y square is it

        Returns:
            True, if square is taken so it is not '-'
        """

        return self.board[y_square][x_square] != '-'

    def check_draw(self):
        """Check if board is full and if it is, sets result to draw and game ends
        """

        if not any('-' in x for x in self.board) and self.result == Result.ONGOING:
            self.result = Result.DRAW
