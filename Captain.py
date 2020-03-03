import pygame
import random

win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Main Menu")

bg = pygame.image.load('CaptainSonarMAp.jpg')
bg = pygame.transform.scale(bg, (1600, 900))

while True:

    win.blit(bg, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()