import pygame
import random
from network import Network

pygame.init()

n = Network()
# startPos = n.getTurn()




win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Captain")

bg = pygame.image.load('SpyMap.png')
bg = pygame.transform.scale(bg, (1920, 1080))

initDot = pygame.image.load('initDot.png')
currentPos = pygame.image.load('currentPos.png')

Thefont = pygame.font.SysFont('comicsans', 60, False, False)

rowDict = {"A": 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15}
rowDictNum = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 14 : "N", 15 : "O"}

# startPos = input("What sector would you like to start? Enter row and column like G3 ")

startPosD = "G6"

rowNum = rowDict[startPosD[0]]
column = int(startPosD[1])



class click(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

aDot = click(153, 157, 7)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

for i in range(1, 16):
    globals()['row%s' % i] = click(107 + (78 * i), 188, 8)
    for k in range(1, 16):
        globals()['dot%s' % rowDictNum[i] + str(k)] = click(globals()['row%s' % i].x, 126 + (58 * k), 8)

width = 5

islandDot = (dotB3, dotB4, dotD6, dotB7, dotD10, dotC11, dotB12, dotB13, dotA14, dotE5, dotF5, dotG4, dotF6,
             dotI6, dotH6, dotG9, dotG10, dotH10, dotJ10, dotJ11, dotK11, dotL6, dotL10, dotM5, dotN3, dotN4,
             dotN9, dotN2, dotO2)

islandDotStr = ('dotB3', 'dotB4', 'dotD6', 'dotB7', 'dotD10', 'dotC11', 'dotB12', 'dotB13', 'dotA14', 'dotE5', 'dotF5', 'dotG4', 'dotF6',
             'dotI6', 'dotH6', 'dotG9', 'dotG10', 'dotH10', 'dotJ10', 'dotJ11', 'dotK11', 'dotL6', 'dotL10', 'dotM5', 'dotN3', 'dotN4',
             'dotN9', 'dotN2', 'dotO2')

currentDot = dotA1
dots = [dotA1, dotA2, dotA3, dotA4, dotA5, dotA6, dotA7, dotA8, dotA9, dotA10, dotA11, dotA12, dotA13, dotA14, dotA15,
        dotB1, dotB2, dotB3, dotB4, dotB5, dotB6, dotB7, dotB8, dotB9, dotB10, dotB11, dotB12, dotB13, dotB14, dotB15,
        dotC1, dotC2, dotC3, dotC4, dotC5, dotC6, dotC7, dotC8, dotC9, dotC10, dotC11, dotC12, dotC13, dotC14, dotC15,
        dotD1, dotD2, dotD3, dotD4, dotD5, dotD6, dotD7, dotD8, dotD9, dotD10, dotD11, dotD12, dotD13, dotD14, dotD15,
        dotE1, dotE2, dotE3, dotE4, dotE5, dotE6, dotE7, dotE8, dotE9, dotE10, dotE11, dotE12, dotE13, dotE14, dotE15,
        dotF1, dotF2, dotF3, dotF4, dotF5, dotF6, dotF7, dotF8, dotF9, dotF10, dotF11, dotF12, dotF13, dotF14, dotF15,
        dotG1, dotG2, dotG3, dotG4, dotG5, dotG6, dotG7, dotG8, dotG9, dotG10, dotG11, dotG12, dotG13, dotG14, dotG15,
        dotH1, dotH2, dotH3, dotH4, dotH5, dotH6, dotH7, dotH8, dotH9, dotH10, dotH11, dotH12, dotH13, dotH14, dotH15,
        dotI1, dotI2, dotI3, dotI4, dotI5, dotI6, dotI7, dotI8, dotI9, dotI10, dotI11, dotI12, dotI13, dotI14, dotI15,
        dotJ1, dotJ2, dotJ3, dotJ4, dotJ5, dotJ6, dotJ7, dotJ8, dotJ9, dotJ10, dotJ11, dotJ12, dotJ13, dotJ14, dotJ15,
        dotK1, dotK2, dotK3, dotK4, dotK5, dotK6, dotK7, dotK8, dotK9, dotK10, dotK11, dotK12, dotK13, dotK14, dotK15,
        dotL1, dotL2, dotL3, dotL4, dotL5, dotL6, dotL7, dotL8, dotL9, dotL10, dotL11, dotL12, dotL13, dotL14, dotL15,
        dotM1, dotM2, dotM3, dotM4, dotM5, dotM6, dotM7, dotM8, dotM9, dotM10, dotM11, dotM12, dotM13, dotM14, dotM15,
        dotN1, dotN2, dotN3, dotN4, dotN5, dotN6, dotN7, dotN8, dotN9, dotN10, dotN11, dotN12, dotN13, dotN14, dotN15,
        dotO1, dotO2, dotO3, dotO4, dotO5, dotO6, dotO7, dotO8, dotO9, dotO10, dotO11, dotO12, dotO13, dotO14, dotO15]

drawLineToggle = False
initDotState = True
posLine = []

myMove = True

startPos = 0
startPos = n.getPos()
p = startPos
p2 = 0

while True:
    (mouseX, mouseY) = pygame.mouse.get_pos()
    # print (mouseX, mouseY)
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    win.blit(bg, (0, 0))


    P1posInDots = dots.index(currentDot)

    p2pos = n.send(str(p))
    P2posInDots = p2pos



    # pygame.draw.circle(win, (255, 0, 0), (currentDot.x, currentDot.y), currentDot.radius)

    # pygame.draw.rect(win, (255,0,0), (aDot.x, aDot.y, aDot.width, aDot.height))

    #Draws The Dots
    for i in range(1, 16):
        if globals()['dot%s' % rowDictNum[i] + str(k)] not in islandDotStr:
            pygame.draw.circle(win, (255, 255, 255), (globals()['dot%s' % rowDictNum[i] + str(k)].x, globals()['row%s' % i].y) , globals()['row%s' % i].radius)
        for k in range(1, 16):
            if 'dot' + rowDictNum[i] + str(k) not in islandDotStr:
                pygame.draw.circle(win, (255, 255, 255), (globals()['dot%s' % rowDictNum[i] + str(k)].x, globals()['dot%s' % rowDictNum[i] + str(k)].y), globals()['dot%s' % rowDictNum[i] + str(k)].radius)
                #print ('dot' + rowDictNum[i] + str(k))



    for dot in dots:
        if initDotState == False:
            if dot.y - 7 < mouseY < dot.y + 7:
                if dot.x - 7 < mouseX < dot.x + 7:
                    if (currentDot.x + 80 > dot.x) and (currentDot.x - 80 < dot.x) and (currentDot.y - 110 < dot.y) and (currentDot.y + 110 > dot.y) and\
                    (dots.index(dot) != P1posInDots + 16) and (dots.index(dot) != P1posInDots - 16) and (dots.index(dot) != P1posInDots + 14) and (dots.index(dot) != P1posInDots - 14):
                        if dot not in islandDot:

                            pygame.draw.circle(win, (20, 255, 20), (dot.x, dot.y), dot.radius)

                            if pressed1:
                                posLine.append(((currentDot.x, currentDot.y), (dot.x, dot.y)))
                                currentDot = dot
                                P1posInDots = dots.index(currentDot)
                                print(P1posInDots)
                    else:
                        pygame.draw.circle(win, (255, 20, 20), (dot.x, dot.y), dot.radius)
        elif initDotState == True:
            if dot not in islandDot:
                if dot.y - 7 < mouseY < dot.y + 7:
                    if dot.x - 7 < mouseX < dot.x + 7:
                        pygame.draw.circle(win, (20, 255, 20), (dot.x, dot.y), dot.radius)
                        if pressed1:
                            currentDot = dot
                            P1posInDots = dots.index(currentDot)
                            print (P1posInDots)
                            initDotState = False

    # pygame.draw.circle(win, (75, 100, 255), (dots[p2pos].x, dots[p2pos].y), currentDot.radius + 5)


    # if initDotState == True:
    #     win.blit(initDot, (1150, 45))
    # elif initDotState == False:
    #     win.blit(currentPos, (1150, 45))
    #     # dot = str(currentDot)
    #     dotPos = Thefont.render("currentDot", 1, (200, 200, 200))
    #     win.blit(dotPos, (1390, 45))

    if initDotState == False:
        pygame.draw.circle(win, (75, 100, 255), (currentDot.x, currentDot.y), currentDot.radius + 5)

    for pos in posLine:
        pygame.draw.line(win, (5, 5, 5), pos[0], pos[1], width)

    pygame.display.update()

    pos = rowDictNum[rowNum] + str(column)
    # print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
