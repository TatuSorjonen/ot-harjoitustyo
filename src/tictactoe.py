import os
import math
import pygame
from tictactoeboard import TicTacToeBoard
from board import Result
from startmenu import StartMenu

class TicTacToe:
    """Ui class for TicTacToe game.

    Attributes:
        start_menu: Starting menu
        board: Tictactoe board
        screen: Pygame window
        x_image: X image
        o_image: O image
        square_size: How big is one square in pixels
        grid_size: Default window size in pixels
        num_squares: How many squares in one row
     """

    def __init__(self):
        """Class constructor, which initializes the variables
        and final values are set later, because they depend on user input

        Attributes:
            start_menu: Starting menu
            board: Tictactoe board
            screen: Pygame window
            x_image: X image
            o_image: O image
            square_size: How big is one square in pixels
            grid_size: Default window size in pixels
            num_squares: How many squares in one row
        """
        self.start_menu = None

        self.board = None
        self.screen = None
        self.x_image = None
        self.o_image = None
        self.square_size = 0
        self.grid_size = 800
        self.num_squares = 0
        self.player1 = ''
        self.player2 = ''
        self.result_text = ''
        self.whose_turn = ''

    def run(self):
        """Function where game runs
        """

        running = True

        self.start_game()

        # If you pressed "Lopeta" button game ends
        if self.num_squares == 0:
            return

        while running and self.num_squares > 0:
            self.play_game(running)

                # If right up x button is pressed quit loop and game ends
                #if event.type == pygame.QUIT: # pylint: disable=no-member
                    #running = False

            if self.board.result == Result.ONGOING:
                pygame.display.flip()

        pygame.quit() # pylint: disable=no-member

    def play_game(self, running):
        for event in pygame.event.get():

            # If button is pressed, draw x or o picture
            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                if event.pos[0] > self.grid_size or event.pos[1] > self.grid_size:
                    continue
                self.draw_xo(event.pos[0], event.pos[1])
                self.draw_status()

            # If game ends, draw winner and new Tkinter window where you can start again
            if self.board.result != Result.ONGOING:

                self.set_result()
                pygame.quit() # pylint: disable=no-member

                self.start_game()

                if self.num_squares == 0:
                    running = False
                    break

        return running

    def start_game(self):
        """Calls function which sets num_squares based on what you pick in starting screen
        and if num_squares is 0 returns. Else sets game variables right with set_game function
        """

        self.start_menu = StartMenu(self.result_text)

        self.get_game_variables()

        if self.num_squares == 0:
            return

        if self.players_name_ok(self.start_menu.name_max_size) is False:
            self.result_text = 'Virheellinen pelaajan nimi'
            self.start_game()
        else:
            self.set_game()

    def get_game_variables(self):
        """Show Tkinter menu and set num_squares to what user gave it in Tkinter window
        """

        self.start_menu.show()
        self.num_squares = self.start_menu.num_squares
        self.player1 = self.start_menu.player1
        self.player2 = self.start_menu.player2


    def players_name_ok(self, max_size):
        player1_len = len(self.player1)
        player2_len = len(self.player2)
        names_ok = True
        if player1_len > max_size or player1_len < 1:
            names_ok = False
        if player2_len > max_size or player2_len < 1:
            names_ok = False
        return names_ok


    def set_game(self):
        """Sets game variables right with right num_squares and then calls draw_grid
        function which draws board right and also draw_status function which draw whose
        turn is it first time (player 1)
        """

        self.board = TicTacToeBoard(self.num_squares)

        self.square_size = int(self.grid_size/self.num_squares)
        self.grid_size = self.grid_size - (self.grid_size % self.num_squares)

        self.x_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/x.png"), (self.square_size, self.square_size))
        self.o_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/o.png"), (self.square_size, self.square_size))

        #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.start_menu.window_width + 50,0)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
        pygame.init() # pylint: disable=no-member
        window_size = [self.grid_size, self.grid_size + 100]
        self.screen = pygame.display.set_mode(window_size, pygame.NOFRAME, pygame.SHOWN) # pylint: disable=no-member

        self.draw_grid()
        self.draw_status()

    def draw_xo(self, mouse_x, mouse_y):
        """Draws X or O picture in right position

        Args:
            x_square and y_square: Check which position you clicked and count which square there is
            x_coordinate and y_coordinate: Define images left upper corner
        """

        x_square = math.floor(mouse_x / self.square_size)
        y_square = math.floor(mouse_y / self.square_size)

        x_coordinate = self.square_size * x_square
        y_coordinate = self.square_size * y_square

        # Check turn and draw right image to pygame window into right square
        if self.board.whose_turn == 1 and not self.board.is_taken(y_square, x_square):
            self.screen.blit(self.x_image, (x_coordinate, y_coordinate))
            self.board.add_x(x_square, y_square)
        elif self.board.whose_turn == 2 and not self.board.is_taken(y_square, x_square):
            self.screen.blit(self.o_image, (x_coordinate, y_coordinate))
            self.board.add_o(x_square, y_square)

    # Draws grid in game
    def draw_grid(self):
        """ Draws grid in board

        Args:
            black: color black (lines)
            gray: color gray (background)

        """

        black = (0, 0, 0)
        gray = (200, 200, 200)

        self.screen.fill((gray))

        for x_int in range(0, self.grid_size, self.square_size):
            for y_int in range(0, self.grid_size, self.square_size):
                rect = pygame.Rect(x_int, y_int, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, black, rect, 1)

    def draw_status(self):
        """Draws status in game, whose turn is it
        """

        if self.board.whose_turn == 1:
            self.whose_turn = f"Vuoro: {self.player1}"
        else:
            self.whose_turn = f"Vuoro: {self.player2}"

        font = pygame.font.SysFont('comicsans', 80)
        text = font.render(self.whose_turn, 1, (0, 0, 0))
        self.screen.fill((200, 200, 200), (0, self.grid_size, self.grid_size + 100, 100))
        text_rect = text.get_rect(center=(self.grid_size/2, self.grid_size + 50))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def set_result(self):
        if self.board.result == Result.FIRST_WIN:
            self.result_text = f"{self.player1} voittaa"
        elif self.board.result == Result.SECOND_WIN:
            self.result_text = f"{self.player2} voittaa"
        elif self.board.result == Result.DRAW:
            self.result_text = 'Tasapeli'
