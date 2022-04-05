import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
HEIGHT = 1000
WIDTH = 1000

pygame.init()

screen = pygame.display.set_mode([HEIGHT, WIDTH])
CLOCK = pygame.time.Clock()
screen.fill((WHITE))

running = True
while running:
    block_size = int(HEIGHT/3)
    for x in range(0, WIDTH, block_size):
        for y in range(0, HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(screen, BLACK, rect, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Flip the display
    pygame.display.flip()

pygame.quit()
