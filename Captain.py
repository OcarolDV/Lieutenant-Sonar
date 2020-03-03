import pygame
import random

win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Main Menu")

bg = pygame.image.load('CaptainSonarMAp.jpg')
bg = pygame.transform.scale(bg, (1600, 900))

rowDict = {"A": 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15}
rowDictNum = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 14 : "N", 15 : "O"}

# startPos = input("What sector would you like to start? Enter row and column like G3 ")
startPos = "G6"

rowNum = rowDict[startPos[0]]
column = int(startPos[1])

class click(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

aRow = click(145, 140, 20, 720)

# for i in range (15):



while True:

    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255,0,0), (aRow.x, aRow.y, aRow.width, aRow.height))

    pygame.display.update()

    pos = rowDictNum[rowNum] + str(column)
    print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()