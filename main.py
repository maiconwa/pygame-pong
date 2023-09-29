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

# colors
back_ground_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# movement
ball_speed_x = 7
ball_speed_y = 7


# runs the game
while True:
    # input handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # game object move
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # screen visuals
    screen.fill(back_ground_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, cpu_opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # update window
    pygame.display.flip()
    clock.tick(60)
