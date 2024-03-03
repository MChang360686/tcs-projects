import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
position_2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
jump = 0

def make_fist(position):
    pygame.draw.circle(screen, "orange", (position.x + 40, position.y), 25)

def make_fist_2(position_2):
    pygame.draw.circle(screen, "green", (position_2.x - 40, position_2.y), 25)


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("purple")

    pygame.draw.circle(screen, "blue", position, 50)

    pygame.draw.circle(screen, "red", position_2, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position.y -= 300 * dt
    if keys[pygame.K_s]:
        position.y += 300 * dt
    if keys[pygame.K_a]:
        position.x -= 300 * dt
    if keys[pygame.K_d]:
        position.x += 300 * dt
    if keys[pygame.K_f]:
        make_fist(position)

    if keys[pygame.K_UP]:
        position_2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        position_2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        position_2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        position_2.x += 300 * dt
    if keys[pygame.K_m]:
        make_fist_2(position_2)
    

    
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()