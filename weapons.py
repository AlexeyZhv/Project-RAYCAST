import pygame as pg
from Math.Ray import *
from Math.Vector import *
from Beam import *
from random import random
import Global as g

Shotgun_tex = []
Pistol_tex = []
FPS = 60
for i in range(1, 14):
    surface = pg.surface.Surface([1200, 800], pg.SRCALPHA)
    surface.blit(pg.image.load(f"sprites/Shotgun/shotgun{i}.png"), [0, 24])
    Shotgun_tex.append(surface)

for i in range(0, 8):
    surface = pg.surface.Surface([1200, 800], pg.SRCALPHA)
    surface.blit(pg.image.load(f"sprites/Pistol/{i}.png"), [0, 24])
    Pistol_tex.append(surface)

class Weapon:
    def __init__(self, animation, cooldown) -> None:
        self.state = 0
        self.timer = 0
        self.animation = animation
        self.cd = cooldown
    def draw(self, surface, shooting):
        if self.state == 0:
            if shooting:
                self.state = 1
                self.timer = 0
            surface.blit(self.animation[0], [0, 0])
        else:
            self.state = 2
            surface.blit(self.animation[int(self.timer * (len(self.animation) - 1) / self.cd) + 1], [0, 0])
            self.timer += 1 / FPS
            if self.timer > self.cd:
                self.state = 0

class Shotgun:
    def __init__(self, player) -> None:
        self.weapon = Weapon(Shotgun_tex, 1.5)
        self.state = self.weapon.state
        self.player = player
        self.shooting = False
    def draw(self, surface, shooting, trigger_pressed):
        self.weapon.draw(surface, shooting)
        self.state = self.weapon.state
    def shoot(self, lmap):
        if self.state == 1:
            for i in range(5):
                ang = self.player.ang + (0.5 - random()) * 0.3
                beam = Beam(
                    lmap, [self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                    ang, 400, 3, 500, 10
                )
                g.BEAMS.append(beam)
                ray = Hitscan([self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                    Vector([0, 1]).set_by_angle(ang), beam.length, lmap)

class Pistol:
    def __init__(self, player) -> None:
        self.weapon = Weapon(Pistol_tex, 0.6)
        self.state = self.weapon.state
        self.player = player
        self.shooting = False
    def draw(self, surface, shooting, trigger_pressed):
        self.weapon.draw(surface, shooting)
        self.state = self.weapon.state
    def shoot(self, lmap):
        if self.state == 1:
            ang = self.player.ang
            beam = Beam(
                    lmap, [self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                    ang, 400, 3, 500, 10
            )
            g.BEAMS.append(beam)
            ray = Hitscan([self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                Vector([0, 1]).set_by_angle(ang), beam.length, lmap)

class Minigun:
    def __init__(self, player) -> None:
        self.weapon = Weapon(Pistol_tex, 0.1)
        self.state = self.weapon.state
        self.player = player
        self.shooting = False
    def draw(self, surface, shooting, trigger_pressed):
        self.weapon.draw(surface, trigger_pressed)
        self.state = self.weapon.state
    def shoot(self, lmap):
        if self.state == 1:
            ang = self.player.ang
            beam = Beam(
                    lmap, [self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                    ang, 400, 3, 500, 10
            )
            g.BEAMS.append(beam)
            ray = Hitscan([self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                Vector([0, 1]).set_by_angle(ang), beam.length, lmap)
            
        

