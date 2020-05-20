import pygame
import random
import Network

pygame.init()

win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Engineer")



bg = pygame.image.load('EngineerScreen.jpg')
bg = pygame.transform.scale(bg, (1920, 1080))

st = pygame.image.load('STcircle.png')
st = pygame.transform.scale(st, (90, 80))
stt = pygame.transform.scale(st, (90, 80))

rx = pygame.image.load('rx.png')
rx = pygame.transform.scale(rx, (90, 68))

rxy = pygame.transform.scale(rx, (90, 58))

Thefont = pygame.font.SysFont('comicsans', 60, False, False)
damage = 0
class blackout(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class box(object):

    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

testBox = box(0, 0, 100, 100)

sRadar = box(760, 390, 90, 70)
sSub1 = box(760, 500, 80, 65)
sSub2 = box(970, 390, 90, 70)
sAtk = box(970, 500, 90, 70)

sRadarX = False
sSub1X = False
sSub2X = False
sAtkX = False

yRadar = box(456, 593, 80, 60)
ySub = box(455, 505, 80, 60)
yAtk = box(261, 506, 80, 60)
yAtk2 = box(1490, 591, 80, 60)

yRadarX = False
ySubX = False
yAtkX = False
yAtk2X = False

rRadar = box(642, 505, 85, 65)
rSub1 = box(1179, 399, 85, 65)
rSub2 = box(1383, 507, 85, 65)
rAtk = box(1383, 398, 85, 65)

rRadarX = False
rSub1X = False
rSub2X = False
rAtkX = False

pressed1 = False

myTurn = False
def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((200, 5, 5))
    for alpha in range(0,300):
        fade.set_alpha(alpha)
        win.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(3)
def crossoutSense(circ):
    if circ.y < mouseY < circ.y + circ.width:
        if circ.x < mouseX < circ.x + circ.length:
            return True

def crossoutClick(circx):
    if pressed1 and circx == False and myTurn == True:
        return True

northCounter = 0
southCounter = 0
westCounter = 0
eastCounter = 0
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pressed1 = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pressed1 = False


    (mouseX, mouseY) = pygame.mouse.get_pos()
    # print (mouseX, mouseY)
    # pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    win.blit(bg, (0, 0))

############################## SILVER PIPE ####################################################################################################

    if testBox.y < mouseY < testBox.y + testBox.width:
        if testBox.x < mouseX < testBox.x + testBox.length:
            pygame.draw.rect(win, (255, 0, 0), (0, 0, 100, 100))
            if pressed1 and myTurn == False:
                myTurn = True

    # top left
    if crossoutSense(sRadar):
        win.blit(rx, (sRadar.x + 4, sRadar.y + 8))
        if crossoutClick(sRadarX):
                sRadarX = True
                myTurn = False
                northCounter += 1
    # Bottom left
    if crossoutSense(sSub1):
        win.blit(rx, (sSub1.x + 4, sSub1.y + 4))
        if crossoutClick(sSub1X):
                sSub1X = True
                myTurn = False
                southCounter += 1

    # Top right
    if crossoutSense(sSub2):
        win.blit(rx, (sSub2.x, sSub2.y + 2))
        if crossoutClick(sSub2X):
                sSub2X = True
                myTurn = False
                northCounter += 1

    # Bottom right
    if crossoutSense(sAtk):
        win.blit(rx, (sAtk.x + 2, sAtk.y + 2))
        if crossoutClick(sAtkX):
            sAtkX = True
            myTurn = False
            southCounter += 1
    if sRadarX == True:
        win.blit(rx, (sRadar.x + 4, sRadar.y + 8))

    if sSub1X == True:
        win.blit(rx, (sSub1.x + 4, sSub1.y + 4))

    if sSub2X == True:
        win.blit(rx, (sSub2.x, sSub2.y + 2))

    if sAtkX == True:
        win.blit(rx, (sAtk.x + 2, sAtk.y + 2))

    if sRadarX == True and sSub1X == True and sSub2X == True and sAtkX == True:
        sRadarX = False
        sSub1X = False
        sSub2X = False
        sAtkX = False
        southCounter -= 2
        northCounter -= 2

############################## SILVER PIPE ####################################################################################################

############################## YELLOW PIPE ####################################################################################################

    # left right
    if crossoutSense(yRadar):
        win.blit(rxy, (yRadar.x, yRadar.y))
        if crossoutClick(yRadarX):
                yRadarX = True
                myTurn = False
                westCounter += 1
    # Left top right
    if crossoutSense(ySub):
        win.blit(rxy, (ySub.x, ySub.y))
        if crossoutClick(ySubX):
                ySubX = True
                myTurn = False
                westCounter += 1
    # left left
    if crossoutSense(yAtk):
        win.blit(rxy, (yAtk.x, yAtk.y))
        if crossoutClick(yAtkX):
            yAtkX = True
            myTurn = False
            westCounter += 1
    # right
    if crossoutSense(yAtk2):
        win.blit(rxy, (yAtk2.x, yAtk2.y))
        if crossoutClick(yAtk2X):
            yAtk2X = True
            myTurn = False
            eastCounter += 1
    if yRadarX == True:
        win.blit(rxy, (yRadar.x, yRadar.y))

    if ySubX == True:
        win.blit(rxy, (ySub.x, ySub.y))

    if yAtkX == True:
        win.blit(rxy, (yAtk.x, yAtk.y))

    if yAtk2X == True:
        win.blit(rxy, (yAtk2.x, yAtk2.y))

    if yRadarX == True and ySubX == True and yAtkX == True and yAtk2X == True:
        yRadarX = False
        ySubX = False
        yAtkX = False
        yAtk2X = False
        eastCounter -= 1
        westCounter -= 3

############################## YELLOW PIPE ####################################################################################################

############################## RED PIPE ####################################################################################################
    # south
    if crossoutSense(rRadar):
        win.blit(rx, (rRadar.x, rRadar.y))
        if crossoutClick(rRadarX):
            rRadarX = True
            myTurn = False
            southCounter += 1
    # north left
    if crossoutSense(rSub1):
        win.blit(rx, (rSub1.x, rSub1.y))
        if crossoutClick(rSub1X):
            rSub1X = True
            myTurn = False
            northCounter += 1
    # right mid left
    if crossoutSense(rSub2):
        win.blit(rx, (rSub2.x, rSub2.y))
        if crossoutClick(rSub2X):
            rSub2X = True
            myTurn = False
            eastCounter += 1
    # Right top left
    if crossoutSense(rAtk):
        win.blit(rx, (rAtk.x, rAtk.y))
        if crossoutClick(rAtkX):
            rAtkX = True
            myTurn = False
            eastCounter += 1


    if rRadarX == True:
        win.blit(rx, (rRadar.x, rRadar.y))

    if rSub1X == True:
        win.blit(rx, (rSub1.x, rSub1.y))

    if rSub2X == True:
        win.blit(rx, (rSub2.x, rSub2.y))

    if rAtkX == True:
        win.blit(rx, (rAtk.x, rAtk.y))

    if rRadarX == True and rSub1X == True and rSub2X == True and rAtkX == True:
        rRadarX = False
        rSub1X = False
        rSub2X = False
        rAtkX = False
        eastCounter -= 2
        northCounter -= 1
        southCounter -= 1

    if southCounter == 3:
        fade(1920,1080)
        southCounter = 0
        sRadar = False
        sSub1 = False
        sAtk = False
        damage += 1
    if northCounter == 3:
        fade(1920,1080)
        northCounter = 0
        sRadarX = False
        sSub2X = False
        rSub1X = False
        damage += 1
    if eastCounter == 3:
        fade(1920,1080)
        eastCounter = 0
        yAtk2X = False
        rSub2X = True
        rAtkX = False
        damage += 1
    if westCounter == 3:
        fade(1920,1080)
        yRadarX = False
        ySubX = False
        yAtkX = False
        westCounter = 0
        damage += 1
############################## RED PIPE ####################################################################################################

    pygame.display.update()
