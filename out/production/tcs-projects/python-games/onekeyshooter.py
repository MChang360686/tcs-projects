import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroid Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

asteroid_sizes = [5, 10, 15, 25, 30, 50]

player_width = 20
player_height = 20

laser_width = 10
laser_height = 10
laser_speed = 5

score = 0
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
game_over = False

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def draw_asteroid(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), random.choice(asteroid_sizes))

def draw_laser(x, y):
    pygame.draw.rect(screen, "green", (x, y, laser_width, laser_height))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def game_loop():
    global game_over, score
    global player_width, player_height, player_speed

    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height
    player_speed = 5

    asteroid_x = random.randint(0, SCREEN_WIDTH - 50)
    asteroid_y = -asteroid_x

    laser_x = player_x
    laser_y = player_y

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        if keys[pygame.K_SPACE]:
            draw_laser(player_x, player_y)

        screen.fill(BLACK)

        draw_player(player_x, player_y)
        draw_asteroid(asteroid_x, asteroid_y)
        draw_laser(laser_x, laser_y)
        asteroid_y -= 5
        laser_y += laser_speed
            
        if asteroid_y > SCREEN_HEIGHT:
            asteroid_x = random.randint(0, SCREEN_WIDTH - 50)
            asteroid_y = -asteroid_x
        

        display_score(score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_loop()