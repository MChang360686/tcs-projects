import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 3

# Laser settings
laser_width = 10
laser_height = 150
laser_speed = 3

# Score
score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
game_over = False

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, obstacle_width, obstacle_height))

def draw_laser(x, y):
    pygame.draw.rect(screen, "green", (x, y, laser_width, laser_height))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def game_loop():
    global game_over, score
    global player_width, player_height, player_speed

    # Player settings
    player_width = 50
    player_height = 50
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height
    player_speed = 5

    obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    
    laser_x = random.randint(0, SCREEN_WIDTH - laser_width)
    laser_y = -laser_x

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed

        screen.fill(BLACK)

        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)
        draw_laser(laser_x, laser_y)


        obstacle_y += obstacle_speed
        laser_y += laser_speed

        if obstacle_y > SCREEN_HEIGHT:
            obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            score += 1

        if laser_y > SCREEN_HEIGHT:
            laser_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            laser_y = -laser_x

        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x \
                and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            game_over = True

        if player_x < laser_x + laser_width and player_x + player_width > laser_x \
                and player_y < laser_y + obstacle_height and player_y + player_height > laser_y:
            game_over = True

        display_score(score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_loop()