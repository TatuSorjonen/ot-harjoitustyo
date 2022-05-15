import os
import math
import pickle
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import pygame
from tictactoeboard import TicTacToeBoard
from tictactoeboard import Result
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
        """
        self.start_menu = None
        self.tictactoeboard = None

        self.screen = None
        self.x_image = None
        self.o_image = None
        self.square_size = 0
        self.grid_size = 800
        self.result_text = ''
        self.whose_turn = ''
        self.background_color = (210, 210, 210)
        self.grid_color = (0, 0, 0)
        self.bottom_height = 100
        self.button_width = self.grid_size / 3
        self.running = True

    def run(self):
        """Function where game runs
        """

        self.start_game()

        if self.tictactoeboard.num_squares == 0:
            return

        while self.running and self.tictactoeboard.num_squares > 0:
            self.play_game()

            if self.tictactoeboard.result == Result.ONGOING and self.running:
                pygame.display.flip()

        pygame.quit() # pylint: disable=no-member

    def play_game(self):
        """Event is running while it ends
        """

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
                self.check_button_pressed(event.pos[0], event.pos[1])
                if self.running is False:
                    break
                if event.pos[0] > self.grid_size or event.pos[1] > self.grid_size:
                    continue
                self.set_xo(event.pos[0], event.pos[1])

            if self.tictactoeboard.result != Result.ONGOING:

                self.set_result()
                pygame.quit() # pylint: disable=no-member

                self.start_game()

                if self.tictactoeboard.num_squares == 0:
                    self.running = False
                    break

    def start_game(self):
        """Call Tkinter Class where you set player names and number of squares.
        If one of player names are incorrect starts again with error message.
        Else call set_game function
        """

        self.start_menu = StartMenu(self.result_text)

        num_squares, player1, player2 = self.get_game_variables()

        self.tictactoeboard = TicTacToeBoard(num_squares, player1, player2)

        if self.tictactoeboard.num_squares == 0:
            return

        if self.players_name_ok(self.start_menu.name_max_size) is False:
            self.result_text = 'Virheellinen pelaajan nimi'
            self.start_game()
        else:
            self.set_game()

    def get_game_variables(self):
        """Show Tkinter menu and set num_squares, player1 and player2 to what user gave it in
        Tkinter window
        """

        self.start_menu.show()
        return self.start_menu.num_squares, self.start_menu.player1, self.start_menu.player2


    def players_name_ok(self, max_size):
        """Check if the player names are the correct size

        Args:
            max_size: what is players name max length

        Returns:
            True, if names are the correct length. Otherwise returns False
        """

        player1_len = len(self.tictactoeboard.player1)
        player2_len = len(self.tictactoeboard.player2)
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

        self.square_size = int(self.grid_size/self.tictactoeboard.num_squares)
        self.grid_size = self.grid_size - (self.grid_size % self.tictactoeboard.num_squares)
        self.button_width = math.floor(self.grid_size / 3)

        self.x_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/x.png"), (self.square_size, self.square_size))
        self.o_image = pygame.transform.scale(pygame.image.load\
        ("src/images_xo/o.png"), (self.square_size, self.square_size))

        os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
        pygame.init() # pylint: disable=no-member
        window_size = [self.grid_size, self.grid_size + self.bottom_height]
        self.screen = pygame.display.set_mode(window_size, pygame.NOFRAME, pygame.SHOWN) # pylint: disable=no-member

        self.draw_grid()
        self.draw_status()
        self.draw_buttons()

    def set_xo(self, mouse_x, mouse_y):
        """Add x or o in table

        Args:
            mouse_x: Check x coordinate which position you clicked with mouse
            mouse_y: Check y coordinate which position you clicked with mouse
        """

        x_square = math.floor(mouse_x / self.square_size)
        y_square = math.floor(mouse_y / self.square_size)

        if self.tictactoeboard.whose_turn == 1 and not \
                                         self.tictactoeboard.is_taken(y_square, x_square):
            self.tictactoeboard.add_x(x_square, y_square)
        elif self.tictactoeboard.whose_turn == 2 and not \
                                            self.tictactoeboard.is_taken(y_square, x_square):
            self.tictactoeboard.add_o(x_square, y_square)

        self.update_board()
        self.draw_status()

    def update_board(self):
        """Draw all x and o in table on board
        """

        self.draw_grid()

        for x_square in range(0, self.tictactoeboard.num_squares):
            for y_square in range(0, self.tictactoeboard.num_squares):
                x_coordinate = self.square_size * x_square
                y_coordinate = self.square_size * y_square
                if self.tictactoeboard.board[y_square][x_square] == 'x':
                    self.screen.blit(self.x_image, (x_coordinate, y_coordinate))
                elif self.tictactoeboard.board[y_square][x_square] == 'o':
                    self.screen.blit(self.o_image, (x_coordinate, y_coordinate))

    def draw_grid(self):
        """Draw grid in game

        """

        self.screen.fill((self.background_color), (0, 0, self.grid_size, self.grid_size))

        for x_int in range(0, self.grid_size, self.square_size):
            for y_int in range(0, self.grid_size, self.square_size):
                rect = pygame.Rect(x_int, y_int, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)

    def draw_status(self):
        """Draws status in game, whose turn is it and also 'Tallenna' button and 'Lataa' button
        """

        my_font = 'arial'
        status_font_size = 45
        font_color = (0, 0, 0)
        status_coordinates = (0, self.grid_size, self.grid_size, self.bottom_height/2)
        status_text_center = (self.grid_size/2, self.grid_size + int(self.bottom_height/4))

        if self.tictactoeboard.whose_turn == 1:
            self.whose_turn = f"Vuoro: {self.tictactoeboard.player1}"
        else:
            self.whose_turn = f"Vuoro: {self.tictactoeboard.player2}"

        font = pygame.font.SysFont(my_font, status_font_size)
        text = font.render(self.whose_turn, 1, font_color)
        self.screen.fill((self.background_color), status_coordinates)
        text_rect = text.get_rect(center=status_text_center)
        self.screen.blit(text, text_rect)

        pygame.display.update()


    def draw_buttons(self):

        save_button_coordinates = (0, self.grid_size + self.bottom_height/2, \
                                   self.button_width, self.bottom_height/2)
        save_button_center = (0 + self.button_width/2, \
                            self.grid_size + int(self.bottom_height * 0.75))
        self.draw_one_button('Tallenna peli', save_button_coordinates, save_button_center)


        download_button_coordinates = (self.button_width, self.grid_size + self.bottom_height/2,\
                                       self.button_width, self.bottom_height/2)
        download_button_center = (self.grid_size / 2,\
                                self.grid_size + int(self.bottom_height * 0.75))
        self.draw_one_button('Lataa peli', download_button_coordinates, download_button_center)


        quit_button_coordinates = (self.button_width * 2, self.grid_size + self.bottom_height/2,\
                                       self.grid_size - 2 * self.button_width, self.bottom_height/2)
        quit_button_center = (self.grid_size - self.button_width/2,\
                                self.grid_size + int(self.bottom_height * 0.75))
        self.draw_one_button('Lopeta peli', quit_button_coordinates, quit_button_center)


        pygame.display.update()

    def draw_one_button(self, button_text, button_coordinates, button_center):
        button_font = 'arial'
        button_font_size = 24
        button_color = (150, 150, 150)
        font_color = (50, 50, 50)
        border_color = (120, 120, 120)

        font = pygame.font.SysFont(button_font, button_font_size)
        text = font.render(button_text, 1, font_color)
        pygame.draw.rect(self.screen,(button_color), button_coordinates)
        pygame.draw.rect(self.screen, border_color, pygame.Rect(button_coordinates), 4, 0)
        text_rect = text.get_rect(center=button_center)
        self.screen.blit(text, text_rect)

    def check_button_pressed(self, mouse_x, mouse_y):
        if 0 < mouse_x < self.button_width and\
           self.grid_size + self.bottom_height/2 < mouse_y < self.grid_size + self.bottom_height:
            self.save_game()

        elif self.button_width < mouse_x < self.button_width * 2 and\
             self.grid_size + self.bottom_height/2 < mouse_y < self.grid_size + self.bottom_height:
            self.load_game()

        elif self.button_width * 2 < mouse_x < self.grid_size and\
             self.grid_size + self.bottom_height/2 < mouse_y < self.grid_size + self.bottom_height:
            self.running = False

    def save_game(self):
        message = 'Tallennus onnistui'
        window_title = 'Tallennus'
        try:
            save_menu = tk.Tk()
            save_menu.withdraw()
            save_filename = tkinter.filedialog.asksaveasfilename(title= "Tallenna tiedosto"\
                            ,filetypes=[("Tictactoe tiedostot", "*.ttt")])
            print('SAVE' + '\n' + save_filename)
            save_menu.destroy()
            with open(save_filename, "wb") as save_file:
                pickle.dump(self.tictactoeboard, save_file)
        except (IOError, TypeError, AttributeError, pickle.PicklingError):
            message = 'Tallennus epäonnistui'
        finally:
            self.print_message(message, window_title)


    def load_game(self):
        message = 'Lataus onnistui'
        window_title = 'Lataus'
        try:
            load_menu = tk.Tk()
            load_menu.withdraw()
            load_filename = tkinter.filedialog.askopenfilename(parent=load_menu, \
                            title= "Lataa tiedosto", \
                            filetypes=[("Tictactoe tiedostot", "*.ttt")])
            load_menu.destroy()
            with open(load_filename, "rb") as load_file:
                self.tictactoeboard = pickle.load(load_file)
        except (IOError, TypeError, AttributeError, pickle.UnpicklingError):
            message = 'Lataus epäonnistui'
        else:
            self.set_game()
            self.update_board()
        finally:
            self.print_message(message, window_title)

    def print_message(self, message, window_title):
        errorwindow = tk.Tk()
        errorwindow.overrideredirect(1)
        errorwindow.withdraw()
        tkinter.messagebox.showinfo(window_title, message)
        errorwindow.destroy()

    def set_result(self):
        """Set result text who wins or is it draw
        """

        if self.tictactoeboard.result == Result.FIRST_WIN:
            self.result_text = f"{self.tictactoeboard.player1} voittaa"
        elif self.tictactoeboard.result == Result.SECOND_WIN:
            self.result_text = f"{self.tictactoeboard.player2} voittaa"
        elif self.tictactoeboard.result == Result.DRAW:
            self.result_text = 'Tasapeli'
