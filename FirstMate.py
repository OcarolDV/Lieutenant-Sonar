import pygame
from pygame.locals import *
pygame.init()
# Button for the circles
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
bg = pygame.image.load('FirstMateMapTest.png')
bg = pygame.transform.scale(bg, (960, 720))
win = pygame.display.set_mode((960, 720))

validPoints = 0


# Draws three boxes and a circle
b1 = Button('arial', 75, 80, white, 3)
b2 = Button('arial', 380, 80, white, 4)
b3 = Button('arial', 700, 80, white, 6)
b4 = Button('arial', 75, 408, white, 3)
b5 = Button('arial', 380, 408, white, 4)
b6 = Button('arial', 700, 408, white, 6)
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
            validPoints -= 1
        elif b2.click(mouse, validPoints):
            print(validPoints)
            validPoints -= 1
        elif b3.click(mouse, validPoints):
            print(validPoints)
            validPoints -= 1
        elif b4.click(mouse, validPoints):
            print(validPoints)
            validPoints -= 1
        elif b5.click(mouse, validPoints):
            print(validPoints)
            validPoints -= 1
        elif b6.click(mouse, validPoints):
            print(validPoints)
            validPoints -= 1

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()