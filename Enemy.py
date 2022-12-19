import pygame as pg
import numpy as np
from textures import *
from ray_module import *
from weapons import *
from Global import *
from Player import *
from Sprites import *
from Beam import *

ork_run = []
for i in range(8):
    sprite = pg.image.load(f"./sprites/enemies/ork_run/ork_run_{i}.png")
    ork_run.append(sprite)


class Enemy:
    def __init__(self, coord, size, spd, health=1, texture=ohno):
        self.coord = np.array(coord)
        self.size = size
        self.spd = spd
        self.sprite = Sprite(self.coord, texture, self.size, 5, 20)
        self.health = health
        self.mem = self.coord
        self.timer = 0

    def __del__(self):
        expl(self.coord)

    def draw(self, lmap, player, surface):
        self.timer += 1 / FPS

        if self.timer >= 0.8:
            self.timer = 0

        self.sprite = Sprite(self.coord, ork_run[int(self.timer / 0.1)], self.size, 5, 20)

        self.sprite.draw(lmap, player, surface)

    def avoid(self, point):
        '''
        enemy will run away from point
        :param point:
        :return:
        '''
        vect = (self.coord - point) / mag(self.coord - point)
        self.coord = self.coord + vect * self.spd / FPS


class Ork(Enemy):
    def __init__(self, coord) -> None:
        super().__init__(coord, [48, 48], 100, 1, ork)
        ENEMIES.append(self)

    def move(self, player, level_map):
        '''
        if enemy sees player, he will move to player, else he will move to last player's posintion
        :param player:
        :param level_map:
        :return:
        '''
        vect = Vector(player.coord - self.coord)
        length = vect.length
        hor_vec, ver_vec, trash, trash = ray(level_map, self.coord, vect.convert_to_angle())

        l_new = min(mag(hor_vec), mag(ver_vec))

        is_mem = 0
        if (l_new >= length):
            self.mem = player.coord
        else:
            vect = Vector(self.mem - self.coord)
            is_mem = 1

        if (vect.length > 60 or is_mem == 1) and vect.length > 5:
            vect = vect.multiply_by_number(self.spd / FPS / vect.length)
            vect_arr = np.array([vect.x, vect.y])
            self.coord = self.coord + vect_arr
            self.sprite.move(self.coord)
        self.coord = self.coord
