import pygame
import random

import LoadingScreen

from networkTutorial import Network


# ajgoiadfoghasdoipfg;ojsdfhng;lhslfdglkajdfglk;sdfjglkdafjg

def main():

    pygame.init()

    win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Main Menu")

    TitleImg = pygame.image.load('Title.png')
    # TitleImg = pygame.transform.scale(TitleImg, (800, 50))

    bg = pygame.image.load('MMs.jpg')
    bg = pygame.transform.scale(bg, (1920, 1080))
    exit = pygame.image.load('ExitGame.png')
    exit = pygame.transform.scale(exit, (640, 360))

    playImg = pygame.image.load('PlayButton.png')
    settingsImg = pygame.image.load('SettingsButton.png')
    creditsImg = pygame.image.load('Credits.png')
    helpImg = pygame.image.load('qMark.png')
    tGray = pygame.image.load('TranslucentGray.png')

    class button(object):

        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height



    counter = 2
    TitleWidth = 800
    TitleHeight = 50
    TitleImg = pygame.transform.scale(TitleImg, (TitleWidth, TitleHeight))
    tGray = pygame.transform.scale(tGray, (1920, 80))


    playD = button(20, 250, 300, 80)
    settingsD = button(20, 400, 598, 104)
    creditsD = button(20, 550, 418, 68)
    helpD = button(20, 700, 84, 82)

    yes = button(700, 575, 195, 100)
    no = button(1025, 575, 195, 100)

    exitState = False

    # def exitState():


    while True:
        keys = pygame.key.get_pressed()
        (mouseX, mouseY) = pygame.mouse.get_pos()

        print(str(mouseX) + " | " + str(mouseY))
        win.blit(bg, (0, 0))
        win.blit(tGray, (0, 60))
        win.blit(TitleImg, (530, 70))

        win.blit(playImg, (20, 250))
        win.blit(settingsImg, (20, 400))
        win.blit(creditsImg, (20, 550))
        win.blit(helpImg, (20, 700))


        # Play Button
        if ((mouseX < playD.x + playD.width) and (mouseX > playD.x)) and ((mouseY < playD.y + playD.height) and (mouseY > playD.y)):
            playImg = pygame.transform.scale(playImg, (314, 110))
            m1, m2, m3 = pygame.mouse.get_pressed()
            if m1:
                LoadingScreen.loadingScreen()
                # DotGAME.dotGame()


        else:
            playImg = pygame.image.load('PlayButton.png')
            playImg = pygame.transform.scale(playImg, (285, 100))


        # Settings Button
        if ((mouseX < settingsD.x + settingsD.width) and (mouseX > settingsD.x)) and ((mouseY < settingsD.y + settingsD.height) and (mouseY > settingsD.y)):
            settingsImg = pygame.transform.scale(settingsImg, (int(settingsD.width * 1.1), int(settingsD.height * 1.1)))

        else:
            settingsImg = pygame.image.load('SettingsButton.png')
            settingsImg = pygame.transform.scale(settingsImg, (settingsD.width, settingsD.height))


        # Credits Button
        if ((mouseX < creditsD.x + creditsD.width) and (mouseX > creditsD.x)) and ((mouseY < creditsD.y + creditsD.height) and (mouseY > creditsD.y)):
            creditsImg = pygame.transform.scale(creditsImg, (int(creditsD.width * 1.1), int(creditsD.height * 1.1)))


        else:
            creditsImg = pygame.image.load('Credits.png')
            creditsImg = pygame.transform.scale(creditsImg, (creditsD.width, creditsD.height))


        # Question Mark Button
        if ((mouseX < helpD.x + helpD.width) and (mouseX > helpD.x)) and ((mouseY < helpD.y + helpD.height) and (mouseY > helpD.y)):
            helpImg = pygame.transform.scale(helpImg, (int(helpD.width * 1.1), int(helpD.height * 1.1)))


        else:
            helpImg = pygame.image.load('qMark.png')
            helpImg = pygame.transform.scale(helpImg, (helpD.width, helpD.height))

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

            # exitState = True
            # while exitState == True:
            #     yes = button(700, 575, 195, 100)
            #     no = button(1025, 575, 195, 100)
            #
            #     keys = pygame.key.get_pressed()
            #     (mouseX, mouseY) = pygame.mouse.get_pos()
            #     win.blit(exit, (640, 360))
            #     if ((mouseX < yes.x + yes.width) and (mouseX > yes.x)) and ((mouseY < yes.y + yes.height) and (mouseY > yes.y)):
            #         if m1:
            #             pygame.quit()
            #             quit()
            #
            #     if ((mouseX < no.x + no.width) and (mouseX > no.x)) and ((mouseY < no.y + no.height) and (mouseY > no.y)):
            #         if m1:
            #             exitState = False

                # pygame.display.update()

                # if keys[pygame.K_ESCAPE]:
                #     exitState = False





        pygame.display.update()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()




main()