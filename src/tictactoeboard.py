from enum import Enum

class Result(Enum):
    """Constants, that tell game situation
    """

    ONGOING = 1
    DRAW = 2
    FIRST_WIN = 3
    SECOND_WIN = 4

class TicTacToeBoard():
    """Class that manages the properties of a tictactoe game data structure

    Attributes:
        num_squares: How many num squares
        board: Two dimensional array ('-' = free square, 'x' = player 1, 'o' = player 2)
        result: Game situation
        player1: player 1 name
        player2: player 2 name
        whose_turn: whose turn is it (1 or 2)
    """

    def __init__(self, num_squares, player1, player2):
        """Class contsructor which set all attributes at starting position

        Args:
            num_squares: How big is tictactoe board. Numbers of rows and columns
            player1: Player 1 name
            player2: Player 2 name
        """

        self.num_squares = num_squares
        self.result = Result.ONGOING
        self.player1 = player1
        self.player2 = player2
        self.board = [['-' for i in range(num_squares)] for j in range(num_squares)]
        self.whose_turn = 1

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
        If so then call the check_winner function.
        And after all places are checked, calls check_draw funcion
        """

        for i in range(0, self.num_squares):
            for j in range(0, self.num_squares):

                if self.board[i][j] == '-':
                    continue
                self.check_winner(i, j)

        self.check_draw()

    def check_winner(self, i, j):
        """Check if someone wins or not (4 in a row).
        First check row, then col. After that diagonals

        Args:
            i: y coordinate on board
            j: x coordinate on board
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

    def set_winner(self, winner):
        """Set winner for game after checking if winner is x or not
        Args:
            winner: Who is winner
        """

        if winner == 'x':
            self.result = Result.FIRST_WIN
        else:
            self.result = Result.SECOND_WIN

    def is_taken(self, y_square, x_square):
        """Check if square is taken

        Args:
            x_square: What x square is it
            y_square: What y square is it

        Returns:
            True, if square is taken, otherwise returns False
        """

        return self.board[y_square][x_square] != '-'

    def check_draw(self):
        """Check if board is full and if it is, sets result to draw and game ends
        """

        if not any('-' in x for x in self.board) and self.result == Result.ONGOING:
            self.result = Result.DRAW
