import pygame as pg
from Math.Ray import *
from Math.Vector import *
from Beam import *
from random import random
from Bullet import *
import Global as g
from Global import *

Shotgun_tex = []
Pistol_tex = []
Sword_tex = []
Shield_tex = []

FPS = 60
for i in range(1, 14):
    surface = pg.surface.Surface([width, height], pg.SRCALPHA)
    surface.blit(pg.image.load(f"sprites/Shotgun/shotgun{i}.png"), [0, 24])
    Shotgun_tex.append(surface)

for i in range(0, 8):
    surface = pg.surface.Surface([width, height], pg.SRCALPHA)
    surface.blit(pg.image.load(f"sprites/Pistol/{i}.png"), [0, 24])
    Pistol_tex.append(surface)

for i in range(0, 8):
    surface = pg.surface.Surface([width, height], pg.SRCALPHA)
    surface.blit(pg.transform.scale(pg.image.load(f"./sprites/characters/swordsman/attack/swordsman_attack_{i}.png"), [width, height]), [0, 0])
    Sword_tex.append(surface)

for i in range(0, 2):
    surface = pg.surface.Surface([width, height], pg.SRCALPHA)
    surface.blit(pg.transform.scale(pg.image.load(f"./sprites/characters/swordsman/shield/shield_{i}.png"), [width, height]), [0, 0])
    Shield_tex.append(surface)

class Weapon:
    def __init__(self, player, animation, cooldown, animation_time) -> None:
        self.player = player
        self.timer = 0
        self.animation = animation
        self.cd = cooldown
        self.state = "ready"
        self.animation_time = animation_time
        self.attacked = False

class Primary(Weapon):

    def __init__(self, player, animation, cooldown, animation_time) -> None:
        super().__init__(player, animation, cooldown, animation_time)

    def draw(self, surface, shooting, trigger_pressed):
        if self.state == "ready":
            surface.blit(self.animation[0], [0, 0])
            if shooting:
                self.state = "attacking"
                self.timer = 0
                self.attacked = False
        elif self.state == "attacking":
            self.timer += 1 / FPS
            if self.timer < self.animation_time:
                surface.blit(self.animation[int(self.timer / self.animation_time * len(self.animation))], [0, 0])
            elif self.timer < self.cd:
                surface.blit(self.animation[0], [0, 0])
            else:
                self.state = "ready"
                surface.blit(self.animation[0], [0, 0])

class Secondary(Weapon):
    def __init__(self, player, animation, cooldown, animation_time) -> None:
        super().__init__(player, animation, cooldown, animation_time)
    def draw(self, surface, shooting, trigger_pressed):
        if not trigger_pressed:
            self.state = "ready"
            surface.blit(self.animation[0], [0, 0])
        elif trigger_pressed:
            self.state = "attacking"
            surface.blit(self.animation[1], [0, 0])


'''class Shotgun:
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
                    ang, 5000, 3, 500, 10
                )
                g.BEAMS.append(beam)
                ray = Hitscan([self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
                    Vector([0, 1]).set_by_angle(ang), beam.length, lmap)
                RAYS.append(ray)'''

class Pistol(Primary):
    def __init__(self, player) -> None:
        super().__init__(player, Pistol_tex, 0.6, 0.6)
    def shoot(self, lmap):
        if self.state == "attacking" and not self.attacked:
            self.attacked = True
            ang = self.player.ang
            Fireball([self.player.coord[0] + 15 * np.cos(self.player.ang), self.player.coord[1] + 15 * np.sin(self.player.ang)],
            Vector([1, 0]).set_by_angle(ang), 2000, self.player
            )

class Sword(Primary):
    def __init__(self, player) -> None:
        super().__init__(player, Sword_tex, 0.8, 0.8)
    def shoot(self, lmap):
        if self.state == "attacking" and not self.attacked:
            if self.timer > 0.3:
                self.attacked = True
                ray = Hitscan(self.player.coord, 
                    Vector([0, 1]).set_by_angle(self.player.ang), 64, lmap)
                RAYS.append(ray)
            
class Shield(Secondary):
    def __init__(self, player) -> None:
        super().__init__(player, Shield_tex, 0, 0)
    def shoot(self, lmap):
        if self.state == "attacking":
            self.player.SHIELDED = True
        elif self.state == "ready":
            self.player.SHIELDED = False

