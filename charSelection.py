import pygame


def CharSelect():
    pygame.init()

    win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("charSelect")
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    bg = pygame.image.load('charSelection.jpg')
    bg = pygame.transform.scale(bg, (1920, 1080))



    class button(object):

        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

    capt = button(75, 180, 360, 580)
    engineer = button(530, 180, 360, 580)
    spy = button(980, 180, 360, 580)
    fmate = button(1450, 180, 360, 580)

    while True:
        (mouseX, mouseY) = pygame.mouse.get_pos()
        print(str(mouseX) + " | " + str(mouseY))
        keys = pygame.key.get_pressed()
        (mouseX, mouseY) = pygame.mouse.get_pos()

        win.blit(bg, (0, 0))
        pygame.display.update()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        if keys[pygame.K_RETURN]:
            import Engineer

        if ((mouseX < capt.x + capt.width) and (mouseX > capt.x)) and ((mouseY < capt.y + capt.height) and (mouseY > capt.y)):
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                import Captain

        if ((mouseX < engineer.x + engineer.width) and (mouseX > engineer.x)) and ((mouseY < engineer.y + engineer.height) and (mouseY > engineer.y)):
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                import Engineer

        if ((mouseX < spy.x + spy.width) and (mouseX > spy.x)) and ((mouseY < spy.y + spy.height) and (mouseY > spy.y)):
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                import Spy

        if ((mouseX < fmate.x + fmate.width) and (mouseX > fmate.x)) and ((mouseY < fmate.y + fmate.height) and (mouseY > fmate.y)):
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                import FirstMateMap


        else:
            playImg = pygame.image.load('PlayButton.png')
            playImg = pygame.transform.scale(playImg, (285, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

CharSelect()