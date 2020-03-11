import pygame
import random

win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Main Menu")

bg = pygame.image.load('CaptainSonarMAp.jpg')
bg = pygame.transform.scale(bg, (1920, 1080))

rowDict = {"A": 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15}
rowDictNum = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 14 : "N", 15 : "O"}

# startPos = input("What sector would you like to start? Enter row and column like G3 ")
startPos = "G6"

rowNum = rowDict[startPos[0]]
column = int(startPos[1])

islandDot = ('dotB3', 'dotB4', 'dotD6', 'dotB7', 'dotD10', 'dotC11', 'dotB12', 'dotB13', 'dotA14', 'dotE5', 'dotF5', 'dotG4', 'dotF6',
             'dotI6', 'dotH6', 'dotG9', 'dotG10', 'dotH10', 'dotJ10', 'dotJ11', 'dotK11', 'dotL6', 'dotL10', 'dotM5', 'dotN3', 'dotN4',
             'dotN9', 'dotN2', 'dotO2')

class click(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # self.width = width
        # self.height = height

aDot = click(153, 157, 7)



# for k in range(15):
#     exec(f'aDot{k} = click(153 + (65 * (int({k})+1)), 157 + (52 * (int({k}) + 1), 10))')
#
# for i in range(15):
#     print(aDot + (1 + i))

for i in range(1, 16):
    globals()['row%s' % i] = click(107 + (78 * i), 188, 8)
    for k in range(1, 16):
        globals()['dot%s' % rowDictNum[i] + str(k)] = click(globals()['row%s' % i].x, 126 + (58 * k), 8)



# for k in range(5):
#     exec(f'cat_{k} = k*2')
#
# print(cat_1)

currentDot = 'dotA1'

while True:
    (mouseX, mouseY) = pygame.mouse.get_pos()
    # print (mouseX, mouseY)
    win.blit(bg, (0, 0))
    # pygame.draw.rect(win, (255,0,0), (aDot.x, aDot.y, aDot.width, aDot.height))
    #pygame.draw.circle(win, (255, 0, 0), (aDot.x, aDot.y), aDot.radius)



    for i in range(1, 16):
        if globals()['dot%s' % rowDictNum[i] + str(k)] not in islandDot:
            pygame.draw.circle(win, (255, 255, 255), (globals()['dot%s' % rowDictNum[i] + str(k)].x, globals()['row%s' % i].y) , globals()['row%s' % i].radius)
        for k in range(1, 16):
            if 'dot' + rowDictNum[i] + str(k) not in islandDot:
                pygame.draw.circle(win, (255, 255, 255), (globals()['dot%s' % rowDictNum[i] + str(k)].x, globals()['dot%s' % rowDictNum[i] + str(k)].y), globals()['dot%s' % rowDictNum[i] + str(k)].radius)
                print ('dot' + rowDictNum[i] + str(k))



    pygame.display.update()

    pos = rowDictNum[rowNum] + str(column)
    # print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()