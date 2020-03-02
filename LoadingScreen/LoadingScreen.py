import pygame
bg = pygame.image.load("loadingScreen.png")
bg = pygame.transform.scale(bg, (800,600))
bg1 = pygame.image.load("loadingScreen1.png")
bg1 = pygame.transform.scale(bg1, (800,600))
bg2 = pygame.image.load("loadingScreen2.png")
bg2 = pygame.transform.scale(bg2, (800,600))
bg3 = pygame.image.load("loadingScreen3.png")
bg3 = pygame.transform.scale(bg3, (800,600))
screen = pygame.display.set_mode((800,600))

while True:
    screen.blit(bg, (0, 0))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(bg1,(0,0))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(bg2, (0, 0))
    pygame.display.update()
    pygame.time.wait(1000)
    screen.blit(bg3, (0, 0))
    pygame.display.update()
    pygame.time.wait(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

