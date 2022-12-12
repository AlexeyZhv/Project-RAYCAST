import pygame as pg
import numpy as np
import Global
from Global import *
pg.init()

class Menu:
    def __init__(self, surface, options, size):
        self.surface = surface
        self.options = options
        self.font = pg.font.SysFont("comicsansms", size)
        self.selected = 0
        self.labels = []
        for text in self.options:
            label = self.font.render(text, True, "RED")
            self.labels.append(label)
        h = self.surface.get_height()
        self.Y = np.linspace(0.3 * h, 0.7 * h, len(self.labels))
    def draw(self):
        while True:
            if self.selected < 0:
                self.selected = len(self.labels) - 1
            elif self.selected >= len(self.labels):
                self.selected = 0

            self.surface.fill("Grey")
            w = self.surface.get_width()
            for i in range(len(self.labels)):
                self.surface.blit(self.labels[i], [w / 2 - self.labels[i].get_width() / 2, self.Y[i] - self.labels[i].get_height() / 2])

            pg.draw.circle(self.surface, "RED", [w / 2 - self.labels[self.selected].get_width() / 2 - self.labels[self.selected].get_height(), self.Y[self.selected]], self.labels[self.selected].get_height() / 5)
            pg.display.update()
            clock.tick(FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True, 0
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.selected -= 1
                    elif event.key == pg.K_RIGHT:
                        self.selected += 1
                    elif event.key == pg.K_SPACE:
                        return False, self.selected

Main_menu = Menu(screen, ["Start game", "Quit"], 50)
Pause_menu = Menu(screen, ["Resume game", "Return to main menu", "Quit"], 50)

def main_menu():
    if Global.MENU:
        finished, selected = Main_menu.draw()
        if finished:
            Global.finished = True
        else:
            Global.MENU = False
            Global.PAUSED = False
            if selected == 0:
                Global.finished = False
            if selected == 1:
                Global.finished = True

def pause_menu():
    if Global.PAUSED:
        finished, selected = Pause_menu.draw()
        if finished:
            Global.finished = True
        else:
            Global.PAUSED = False
            if selected == 0:
                Global.PAUSED = False
                Global.finished = False
            elif selected == 1:
                Global.PAUSED = False
                Global.MENU = True
                Global.finished = False
            if selected == 2:
                Global.finished = True