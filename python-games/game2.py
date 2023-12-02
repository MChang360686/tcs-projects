import pygame
import time
import random


pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Duck Hunt")

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        pygame.draw.rect(canvas, (255, 255, 255), (60, 60, 30, 30))
        pygame.display.update()