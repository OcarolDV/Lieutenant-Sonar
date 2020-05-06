import pygame
import sys
vec = pygame.math.Vector2

class TextBox:
    pygame.font.init()
    def __init__(self, x, y, width, height, bg_color = (124, 124, 124), active_color = (255, 255, 255),
                 textSize = 24, text_color = (0,0,0), border = 0, border_color = (0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos= vec(x, y)
        self.size = vec(width, height)
        self.image = pygame.Surface((width, height))
        self.bg_color = bg_color
        self.active_color = active_color
        self.active = False
        self.text = ""
        self.textSize = textSize
        self.font = pygame.font("comic sands", self.textSize)
        self.border_color = border_color
        self.border = border
        self.numbers = [48,49, 50, 51, 53, 54, 55, 56, 57,
                        256,257,258,259,260,261,262,263,264,265]
        self.special = [8, 32]

    def update(self):
        pass

    def draw(self, window):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.bg_color)
            else:
                self.image.fill(self.border_color,
                                (self.border, self.width - self.border*2,
                                 self.height - self.border*2))
            text = self.font.render(self.text, False, self.text_color)

            text_height = text.get_height()
            self.image.blit(text, (self.border*2, (self.height - text_height)//2))
        else:
            if self.border == 0:
                self.image.fill(self.active_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.active_color,
                                 (self.border, self.border, self.width-self.border*2,
                                  self.height-self.border*2))
            text = self.font.render(self.text, False, self.text_color)

            text_height = text.get_height()
            text_width = text.get_width()
            if text_width < self.width-self.border*2:
                self.image.blit(text, (self.border*2, (self.height - text_height)//2))

        window.blit(self.image, self.pos)
    def add_text(self, key):
        try:
            if key in self.numbers:
                text = list(self.text)
                if key<100:
                    text.append(str(key-48))
                else:
                    text.append(str(key-256))
                self.text = ''.join(text)
            elif key == 8:
                text = list(self.text)
                text.pop()
                self.text = ''.join(text)
            elif key == 32:
                text = list(self.text)
                text.append(' ')
                self.text = ''.join(text)


            elif chr(key).isalpha():
                text = list(self.text)
                text.append(chr(key))
                self.text = ' '.join(text)
                print(self.text)
            else:
                print(key)
        except:
            print(key)

    def check_click(self, pos):
        if pos[0] > self.y and pos[1] < self.x-self.width:
            if pos[1] > self.y and pos[1] < self.y-self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

    def return_value(self):
        return self.text









