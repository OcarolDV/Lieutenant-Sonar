import pygame
import sys
from Chat.textBoxClass import *
pygame.init()
window = pygame.display.set_mode((500, 500))
textBoxes = []
textBoxes.append(TextBox(40, 100, 200, 50, border=3))
# textBoxes.append(TextBox(40,100, 200, 50, text_size  = 36))
while True:
    window.fill((54, 54, 54))
    for event in pygame.event.get():
        if event.type == pygame.quit():
            pygame.quit()
           # sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in textBoxes:
                box.check_click(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            for box in textBoxes:
                if box.active:
                    box.add_text(event.key)

    for box in textBoxes:
        box.draw(window)
    pygame.display.update()
