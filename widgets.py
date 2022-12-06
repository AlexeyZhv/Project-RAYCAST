import pygame as pg
class Button:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.pressed = False
    def get_pressed(self):
        self.pressed = False
        x, y = pg.mouse.get_pos()
        if x <= self.pos[0] + self.size[0] and x >= self.pos[0] and y <= self.pos[1] + self.size[1] and y >= self.pos[1]:
            left, middle, right = pg.mouse.get_pressed()
            if left:
                self.pressed = True
        return self.pressed
    def draw(self, screen):
        pg.draw.rect(screen, "RED", [self.pos, self.size])


