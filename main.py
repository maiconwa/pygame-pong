import sys
import pygame

# setup
pygame.init()
clock = pygame.time.Clock()

# main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# game objects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
cpu_opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# runs the game
while True:
    # input handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update window
    pygame.display.flip()
    clock.tick(60)