import pygame
import charSelection

def loadingScreen():
    pygame.init()
    # bg = pygame.image.load("loadingScreen.png")
    # bg = pygame.transform.scale(bg, (800,600))
    bg1 = pygame.image.load("loadingScreen1.png")
    bg1 = pygame.transform.scale(bg1, (1920,1080))
    bg2 = pygame.image.load("loadingScreen2.png")
    bg2 = pygame.transform.scale(bg2, (1920,1080))
    bg3 = pygame.image.load("loadingScreen3.png")
    bg3 = pygame.transform.scale(bg3, (1920,1080))
    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while True:
        keys = pygame.key.get_pressed()
        # screen.blit(bg, (0, 0))
        # pygame.display.update()
        pygame.time.wait(500)

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if keys[pygame.K_RETURN]:
            charSelection.CharSelect()

        screen.blit(bg1,(0,0))
        pygame.display.update()
        pygame.time.wait(500)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if keys[pygame.K_RETURN]:
            charSelection.CharSelect()

        screen.blit(bg2, (0, 0))
        pygame.display.update()
        pygame.time.wait(500)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if keys[pygame.K_RETURN]:
            charSelection.CharSelect()

        screen.blit(bg3, (0, 0))
        pygame.display.update()
        pygame.time.wait(500)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        if keys[pygame.K_RETURN]:
            charSelection.CharSelect()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

