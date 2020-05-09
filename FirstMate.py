import pygame
from pygame.locals import *
pygame.init()
# Button for the circles
class Square:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    def change(self):
        self.color = red
        #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    def clear(self):
        self.color = white

class Button:
    def __init__(self, text, x, y, color, max):
        # Sets variables
        self.max = max
        self.activePoints = 0
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 200
        self.height = 180

    def draw(self, win):
        # Draws to the screen using the variables declared above
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        # Sets the font and size
        font = pygame.font.SysFont("comicsans", 40)
        # Renders the font
        text = font.render(self.text, 1, (255,255,255))
        # Tells where the text should be
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def points(self):
        return self.activePoints - 1

    def click(self, pos, points):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if points > 0:
                    if self.max > self.activePoints:
                        self.activePoints += 1
                        return True
                    else:
                        print("At max")
                        return False
        else:
            return False

# Colors
white = (255, 255, 255)
black = (0, 0, 0,)
red = (255, 0, 0)
green = (0,255,0)
blue = (0, 0, 255)

# Screen
bg = pygame.image.load('CapSonar Image to Edit/first-mate-map_done.png')
bg = pygame.transform.scale(bg, (1920,1080))
win = pygame.display.set_mode((1920, 1080))

validPoints = 0


# Draws three boxes and a circle
b1 = Button('arial', 285, 300, white, 3)
r1 = [Square(390,260, 100, 60, white), Square(480, 300, 75, 90, white), Square(475,390,80,90,white)]

b2 = Button('arial', 855, 300, white, 4)
r2 = [Square(950,260,105,60,white), Square(1050,300,70,80,white), Square(1045,390,80,75,white), Square(950,450,120,55, white)]

b3 = Button('arial', 1425, 300, white, 6)
r3 = [Square(1525,265,100,50,white), Square(1607,310,75,75,white),Square(1600,385,78,78,white), Square(1520, 450, 110, 60, white),Square(1420, 460, 95, 55, white), Square(1350, 375, 80, 90, white)]

b4 = Button('arial', 285, 700, white, 3)
r4 = [Square(390,650, 100, 60, white), Square(480, 690, 75, 90, white), Square(475,780,80,90,white)]

b5 = Button('arial', 855, 700, white, 4)
r5 = [Square(950,650,105,60,white), Square(1050,690,70,80,white), Square(1045,780,80,75,white), Square(950,840,120,55, white)]

b6 = Button('arial', 1425, 700, white, 6)
r6 = [Square(1525,650,100,50,white), Square(1610,695,75,75,white),Square(1607,780,78,78,white), Square(1520, 855, 110, 60, white),Square(1420, 865, 95, 55, white), Square(1350, 780, 80, 90, white)]
# Boxes are around the circle

# Makes button on the circle
# If clicked it checks to see if you have any points
# If you have no points the circle turns red
# If you have a point it turns green
# One box gets filled in with a different color
# Once all the boxes are filled and clicked again they clear
# Push m to get a point
# Points are displayed at the top right

while True:
    # Draws them behind the image
    b5.draw(win)
    b6.draw(win)
    b4.draw(win)
    b3.draw(win)
    b2.draw(win)
    b1.draw(win)
    # Draws first buttons
    for r in range(len(r1)):
        r1[r].draw()
    for r in range(len(r2)):
        r2[r].draw()
    for r in range(len(r3)):
        r3[r].draw()
    for r in range(len(r4)):
        r4[r].draw()
    for r in range(len(r5)):
        r5[r].draw()
    for r in range(len(r6)):
        r6[r].draw()


    # Image
    win.blit(bg, (0, 0))

    for event in pygame.event.get():

        # temp for when you are able to get points
        if event.type == KEYDOWN and event.key == K_EQUALS:
            validPoints += 1

        # gets the mouse position
        mouse = pygame.mouse.get_pos()

        # checks to see when the first button was pressed
        if b1.click(mouse, validPoints):
            print(validPoints)
            r1[b1.points()].change()
            validPoints -= 1
        elif b2.click(mouse, validPoints):
            print(validPoints)
            r2[b2.points()].change()
            validPoints -= 1
        elif b3.click(mouse, validPoints):
            print(validPoints)
            r3[b3.points()].change()
            validPoints -= 1
        elif b4.click(mouse, validPoints):
            print(validPoints)
            r4[b4.points()].change()
            validPoints -= 1
        elif b5.click(mouse, validPoints):
            print(validPoints)
            r5[b5.points()].change()
            validPoints -= 1
        elif b6.click(mouse, validPoints):
            print(validPoints)
            r6[b6.points()].change()
            validPoints -= 1

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
    pygame.display.update()