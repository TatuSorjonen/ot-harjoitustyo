import pygame

class Grid:
    
    def __init__(self, grid_size, num_squares, num_for_win):    
        self.BLACK = (0, 0, 0)
        self.WHITE = (200, 200, 200)
        self.grid_size = grid_size
        self.num_squares = num_squares
        self.num_for_win = num_for_win
        self.block_size = int(self.grid_size/self.num_squares)
              
        pygame.init()
        self.screen = pygame.display.set_mode([self.grid_size, self.grid_size])
        self.screen.fill((self.WHITE))
        
        self.running = True

    def run(self):
        while self.running:
            self.draw_grid()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        pygame.quit()
        
    def draw_grid(self):
        for x in range(0, self.grid_size, self.block_size):
            for y in range(0, self.grid_size, self.block_size):
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

