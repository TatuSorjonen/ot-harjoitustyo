from enum import Enum

class Result(Enum):

    # All game variables, which tells what is games situation right now
    ONGOING = 1
    DRAW = 2
    FIRST_WIN = 3
    SECOND_WIN = 4

class Board:

    def __init__(self, num_squares):

        # Class variables
        self.num_squares = num_squares
        self.board = [[]]
        self.result = Result.ONGOING

    def print_board(self):
        for i in self.board:
            print(i)
