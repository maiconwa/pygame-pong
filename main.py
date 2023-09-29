import sys
import pygame
import random


# animation function
def ball_animation():
    global ball_speed_x, ball_speed_y
    # game object move
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    # game collision
    if ball.colliderect(player) or ball.colliderect(cpu_opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def cpu_opponent_animation():
    if cpu_opponent.top < ball.y:
        cpu_opponent.top += cpu_opponent_speed
    if cpu_opponent.bottom > ball.y:
        cpu_opponent.y -= cpu_opponent_speed
    if cpu_opponent.top <= 0:
        cpu_opponent.top = 0
    if cpu_opponent.bottom >= screen_height:
        cpu_opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, - 1))
    ball_speed_x *= random.choice((1, - 1))


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
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
cpu_opponent_speed = 7

# runs the game
while True:
    # input handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # ball animation
    ball_animation()

    # player animation
    player_animation()

    # cpu opponent animation
    cpu_opponent_animation()

    # screen visuals
    screen.fill(back_ground_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, cpu_opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # update window
    pygame.display.flip()
    clock.tick(60)
