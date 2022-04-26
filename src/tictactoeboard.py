from board import Board
from board import Result

class TicTacToeBoard(Board):

    def __init__(self, num_squares):
        super().__init__(num_squares)
        self.board = [['-' for i in range(num_squares)] for j in range(num_squares)]
        self.whose_turn = 1

    def add_x(self, x_square, y_square):
        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'x'
            self.whose_turn = 2
        self.check_situation()

        #Debug: remove later
        self.print_board()

    def add_o(self, x_square, y_square):
        if not self.is_taken(y_square, x_square):
            self.board[y_square][x_square] = 'o'
            self.whose_turn = 1
        self.check_situation()

        #Debug: remove later
        self.print_board()

    def check_situation(self):
        for i in range(0, self.num_squares):
            for j in range(0, self.num_squares):
                #print(i, ",", j)
                if self.board[i][j] == '-':
                    continue
                self.check_winner(i, j)

        self.check_draw()

    def check_winner(self, i, j):
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
        if winner == 'x':
            self.result = Result.FIRST_WIN
        else:
            self.result = Result.SECOND_WIN

    def print_board(self):
        for i in self.board:
            print(i)
        print()

    def is_taken(self, y_square, x_square):
        return self.board[y_square][x_square] != '-'

    def check_draw(self):
        if not any('-' in x for x in self.board) and self.result == Result.ONGOING:
            self.result = Result.DRAW
