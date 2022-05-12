import tkinter as tk
from functools import partial

class StartMenu:
    """Starting menu class using Tkinter library.\
       There you can choose how big is board 5 to 30 squares
       and what player names are

    Attributes:
        root: Set Tkinter
        num_squares: Set starting num_squares
        player1: Name for player 1
        player2: Name for player 2
    """

    def __init__(self, previous_result = 0):
        """Class constructor, set variables at starting point
        """

        self.root = tk.Tk()
        self.num_squares = 0
        self.player1 = ""
        self.player2 = ""
        self.name_max_size = 10
        self.window_width = 600
        self.window_height = 450
        self.previous_result = previous_result


    def show(self):
        """Shows starting screen with Entrys, Slider and Buttons
        """

        self.set_window()
        self.set_result()

        slider_heading = tk.Label(self.root, text = "Valitse laudan koko", padx = 0, pady = 0)
        slider_heading.pack()
        slider = tk.Scale(self.root, from_=5, to=30,\
                       orient=tk.HORIZONTAL, sliderlength=200, length=500, width=30)
        slider.pack()

        player1_name, player2_name = self.set_players()

        start_button = tk.Button(self.root, text='Aloita peli', height=3, width=25, \
                       command = partial(self.set_num_squares, slider, player1_name, player2_name))
        start_button.pack()
        end_button = tk.Button(self.root, text='Poistu', height=3, width=25, command = self.hide)
        end_button.pack()
        self.root.mainloop()

    def set_window(self):
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        self.root.resizable(False, False)
        self.root.title('Aloita uusi ristinolla-peli')

    def set_result(self):
        if self.previous_result != '':
            result = tk.Label(self.root, text=f'{self.previous_result}',\
                              height ="2", font="Helvetica 23 bold", fg="green")
            result.pack()
        else:
            self.set_empty_row()

    def set_empty_row(self):
        empty = tk.Label(self.root, text='     \n   ', height ="1")
        empty.pack()

    def set_players(self):
        hint = f"(1-{self.name_max_size} merkkiä)"

        self.set_empty_row()
        player1_text = tk.Label(self.root, pady="10", text = "Pelaaja 1 " + hint)
        player1_text.pack()
        player1_name = tk.Entry(self.root, width = 30)
        player1_name.pack()

        player2_text = tk.Label(self.root, pady="10", text = "Pelaaja 2 " + hint)
        player2_text.pack()
        player2_name = tk.Entry(self.root, width = 30)
        player2_name.pack()
        self.set_empty_row()

        return player1_name, player2_name

    # Sets slider valuable into num_squares and destroy window
    def set_num_squares(self, slider, player1_name, player2_name):
        """Set slider valuable into num_squares and player names\
        into player1 and player2 and calls hide
        function after user press 'Aloita peli' button

        Args:
            slider: Slider at starting screen
            player1: Player1 name at starting screen
            player2: player2 name at starting screen
        """

        self.num_squares = slider.get()
        self.player1 = player1_name.get()
        self.player2 = player2_name.get()
        self.hide()

    def hide(self):
        """Destroys window
        """

        self.root.destroy()
