import math
import pygame
from tictactoeboard import TicTacToeBoard
from board import Result

class TicTacToe:

    def __init__(self, grid_size, num_squares):

        #Create new tictactoe board
        self.board = TicTacToeBoard(num_squares)

        # Class variables
        self.grid_size = grid_size # window size in pixels
        self.num_squares = num_squares # how many squares in one row
        self.square_size = int(self.grid_size/self.num_squares) # how big is one square in pixels

        # Images
        self.x_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/x-icon-white-20.jpg"), (self.square_size, self.square_size))
        self.o_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/png_letter_o_51833.png"), (self.square_size, self.square_size))

        # Draw pygame window
        pygame.init() # pylint: disable=no-member
        self.screen = pygame.display.set_mode([self.grid_size, self.grid_size])

    # Game runs while this function is going on
    def run(self):
        running = True

        #self.screen.fill((200,200,200))
        #largeFont = pygame.font.SysFont('comicsans', 80)
        #currentScore = largeFont.render(self.board.winner,1,(0,0,0))
        #self.screen.blit(currentScore, (self.grid_size/2 - currentScore.get_width()/2, 240))
        #pygame.display.update()
        #while True:
        #    continue

        self.draw_grid()
        while running:
            for event in pygame.event.get():

                # If button is pressed draw x or o picture
                if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                    self.draw_xo(event.pos[0], event.pos[1])

                # If game ends anyway for loop ends
                if self.board.result != Result.ONGOING:
                    self.screen.fill((200, 200, 200))
                    font = pygame.font.SysFont('comicsans', 80)
                    who_wins = font.render(self.board.winner, 1, (0, 0, 0))
                    self.screen.blit(who_wins, (self.grid_size/2 - who_wins.get_width()/2, 240))
                    pygame.display.update()
                if event.type == pygame.QUIT: # pylint: disable=no-member
                    running = False

            pygame.display.flip()

        pygame.quit() # pylint: disable=no-member

    def draw_xo(self, mouse_x, mouse_y):

        # Check which position you clicked and count which square there is
        x_square = math.floor(mouse_x / self.square_size)
        y_square = math.floor(mouse_y / self.square_size)

        # Define images left upper corner
        x_coordinate = self.square_size * x_square
        y_coordinate = self.square_size * y_square

        # Check turn and draw right image to pygame window into right square
        if self.board.whose_turn == 1 and not self.board.is_taken(y_square, x_square):
            self.screen.blit(self.x_image, (x_coordinate, y_coordinate))
            self.board.add_x(x_square, y_square)
        elif self.board.whose_turn == 2 and not self.board.is_taken(y_square, x_square):
            self.screen.blit(self.o_image, (x_coordinate, y_coordinate))
            self.board.add_o(x_square, y_square)

    def draw_grid(self):

        black = (0, 0, 0) # Square lines colour
        gray = (200, 200, 200) # Background colour

        # Fill screen with background colour (gray)
        self.screen.fill((gray))

        # Draw square lines (black)
        for x_int in range(0, self.grid_size, self.square_size):
            for y_int in range(0, self.grid_size, self.square_size):
                rect = pygame.Rect(x_int, y_int, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, black, rect, 1)

    def print_message(self, message):
        print(message)
