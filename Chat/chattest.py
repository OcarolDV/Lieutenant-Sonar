import pygame
screen = pygame.display.set_mode((800,600))
bg = pygame.image.load('MMs.jpg')
bg = pygame.transform.scale(bg, (1600, 900))
typeBox = pygame.draw.rect()
while True:
    win = pygame.display.set_mode((1600, 900))
    win.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()