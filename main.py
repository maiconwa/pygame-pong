import sys
import pygame
import random


# Animation function
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, cpu_opponent_score, score_time

    # Game object move
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        cpu_opponent_score += 1
        score_time = pygame.time.get_ticks()

    # game collision
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)

        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1

        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(cpu_opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)

        if abs(ball.left - cpu_opponent.left) < 10:
            ball_speed_x *= -1

        elif abs(ball.bottom - cpu_opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1

        elif abs(ball.top - cpu_opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


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


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - int(score_time) < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width /
                    2 - 10, screen_height / 2 + 20))

    if 700 < current_time - int(score_time) < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width /
                    2 - 10, screen_height / 2 + 20))

    if 1400 < current_time - int(score_time) < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width /
                    2 - 10, screen_height / 2 + 20))

    if current_time - int(score_time) < 2100:
        ball_speed_x, ball_speed_y = 0, 0

    else:
        ball_speed_y = 7 * random.choice((1, - 1))
        ball_speed_x = 7 * random.choice((1, - 1))
        score_time = None


# Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Global variables
back_ground_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
player_score = 0
cpu_opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

# Game objects
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
cpu_opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

# Movement
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
cpu_opponent_speed = 7

# Timer
score_time = True

# Game
while True:
    # Input handler
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

    # Ball animation
    ball_animation()

    # Player animation
    player_animation()

    # Cpu opponent animation
    cpu_opponent_animation()

    # Screen visuals
    screen.fill(back_ground_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, cpu_opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2,
                       0), (screen_width / 2, screen_height))

    # Score
    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))

    cpu_opponent_text = game_font.render(
        f"{cpu_opponent_score}", False, light_grey)
    screen.blit(cpu_opponent_text, (600, 470))

    # Update window
    pygame.display.flip()
    clock.tick(60)
