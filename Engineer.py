import pygame
import random

pygame.init()

win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Engineer")

bg = pygame.image.load('EngineerScreen.jpg')
bg = pygame.transform.scale(bg, (1920, 1080))

Thefont = pygame.font.SysFont('comicsans', 60, False, False)

class blackout(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

changeMe = blackout(153, 157, 30)

while True:
    (mouseX, mouseY) = pygame.mouse.get_pos()
    print (mouseX, mouseY)
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    win.blit(bg, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()