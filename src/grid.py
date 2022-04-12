import pygame


class Grid:

    def __init__(self, grid_size, num_squares, num_for_win):
        self.black_grid = (0, 0, 0)
        self.white_grid = (200, 200, 200)
        self.grid_size = grid_size
        self.num_squares = num_squares
        self.num_for_win = num_for_win
        self.block_size = int(self.grid_size/self.num_squares)
        self.whose_turn = 1
        self.how_many_characters = 0
        #Images
        self.x_image = pygame.transform.scale(pygame.image.load("src/Images/x-icon-white-20.jpg"),(self.block_size, self.block_size))
        self.o_image = pygame.transform.scale(pygame.image.load("src/Images/png_letter_o_51833.png"), (self.block_size, self.block_size))
        pygame.init()
        self.screen = pygame.display.set_mode([self.grid_size, self.grid_size])
        self.screen.fill((self.white_grid))
        self.running = True

    def run(self):
        while self.running:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.draw_xo(event)
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
        pygame.quit()

    def draw_xo(self, event):
        x_coordinate = event.pos[0]-self.x_image.get_width()/2
        y_coordinate = event.pos[1]-self.x_image.get_width()/2
        if self.whose_turn == 1 and self.num_squares*self.num_squares > self.how_many_characters:
            self.screen.blit(self.x_image, (x_coordinate, y_coordinate))
            self.whose_turn = 2
            self.how_many_characters = self.how_many_characters + 1
        elif self.whose_turn == 2 and self.num_squares*self.num_squares > self.how_many_characters:
            self.screen.blit(self.o_image, (x_coordinate, y_coordinate))
            self.whose_turn = 1
            self.how_many_characters = self.how_many_characters + 1
          

    def draw_grid(self):
        for x_int in range(0, self.grid_size, self.block_size):
            for y_int in range(0, self.grid_size, self.block_size):
                rect = pygame.Rect(x_int, y_int, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, self.black_grid, rect, 1)
