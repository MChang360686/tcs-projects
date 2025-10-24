import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("Tunnel Rush Py")

d6 = [1, 2, 3, 4, 5 , 6]

clock = pygame.time.Clock()

shape = pygame.Surface((300, 300))
shape.fill(WHITE)
shape_rect = pygame.draw.rect(shape, "red", pygame.Rect(WIDTH // 2, HEIGHT // 2, 100, 100))


def rotate_left(angle, s):
    if angle >= 360:
        angle = 0
    else:
        angle += 5
    pygame.transform.rotate(s, angle)

def rotate_right(angle, s):
    angle -= 5
    pygame.transform.rotate(s, angle)

def draw_player():
    pygame.draw.rect(screen, "green", (310, 310, 15, 15))

def run_game():
    run = True
    angle = 0
    while run:

        shape_rect = pygame.draw.rect(shape, "red", pygame.Rect(WIDTH // 2, HEIGHT // 2, 100, 100))

        for event in pygame.event.get():       
            if event.type == pygame.QUIT: 
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rotate_left(angle, shape_rect)
        if keys[pygame.K_RIGHT]:
            rotate_right(angle, shape_rect)

        draw_player()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

run_game()