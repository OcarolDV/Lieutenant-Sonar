import pygame
bg = pygame.image.load("FirstMateMapTest.png")
bg = pygame.transform.scale(bg, (1920,1080))
screen = pygame.display.set_mode((1920,1080))
while(True):

    for event in pygame.event.get():
        screen.blit(bg, (0, 0))
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
