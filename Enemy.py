import pygame as pg
import numpy as np
from textures import *
from ray_module import *
from weapons import *
from Global import *
from Player import *
from Sprites import *
from Beam import *


class Enemy:
    def __init__(self, pos, size, spd, health=1, texture=target):
        self.pos = np.array(pos)
        self.size = size
        self.spd = spd
        self.sprite = Sprite(self.pos, texture, self.size, 5, 20)
        self.health = health
        self.mem = self.pos
        self.vect = None
        self.hor_vec = None
        ENEMIES.append(self)

    def __del__(self):
        expl(self.pos)

    def draw(self, lmap, player, surface):
        self.sprite.draw(lmap, player, surface)

    def move(self, player, level_map):
        vect = Vector(player.coord - self.pos)
        length = vect.length
        hor_vec, ver_vec, trash, trash = ray(level_map, self.pos, vect.convert_to_angle())

        l_new = min(mag(hor_vec), mag(ver_vec))

        if (l_new >= length):
            self.mem = player.coord
        else:
            vect = Vector(self.mem - self.pos)

        self.vect = np.array([vect.x, vect.y])
        self.hor_vec = hor_vec

        if vect.length > 30:
            vect = vect.multiply_by_number(self.spd / FPS / vect.length)
            vect_arr = np.array([vect.x, vect.y])
            self.pos = self.pos + vect_arr
            self.sprite.move(self.pos)
