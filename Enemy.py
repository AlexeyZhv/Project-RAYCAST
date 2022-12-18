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
    def __init__(self, coord, size, spd, health=1, texture=target):
        self.coord = np.array(coord)
        self.size = size
        self.spd = spd
        self.sprite = Sprite(self.coord, texture, self.size, 5, 20)
        self.health = health
        self.mem = self.coord

    def __del__(self):
        expl(self.coord)

    def draw(self, lmap, player, surface):
        self.sprite.draw(lmap, player, surface)

    def avoid(self, point):
        '''
        enemy will run away from point
        :param point:
        :return:
        '''
        vect = (self.coord - point) / mag(self.coord - point)
        self.coord = self.coord + vect * self.spd / FPS

class Ork:
    def __init__(self, coord) -> None:
        self.enemy = Enemy(coord, [48, 48], 100, 1, ork)
        self.coord = self.enemy.coord
        self.size = self.enemy.size
        self.health = self.enemy.health
        ENEMIES.append(self)
    def draw(self, lmap, player, surface):
        self.enemy.draw(lmap, player, surface)
    def move(self, player, level_map):
        '''
        if enemy sees player, he will move to player, else he will move to last player's posintion
        :param player:
        :param level_map:
        :return:
        '''
        vect = Vector(player.coord - self.enemy.coord)
        length = vect.length
        hor_vec, ver_vec, trash, trash = ray(level_map, self.enemy.coord, vect.convert_to_angle())

        l_new = min(mag(hor_vec), mag(ver_vec))

        is_mem = 0
        if (l_new >= length):
            self.enemy.mem = player.coord
        else:
            vect = Vector(self.enemy.mem - self.enemy.coord)
            is_mem = 1

        if (vect.length > 60 or is_mem == 1) and vect.length > 5:
            vect = vect.multiply_by_number(self.enemy.spd / FPS / vect.length)
            vect_arr = np.array([vect.x, vect.y])
            self.enemy.coord = self.enemy.coord + vect_arr
            self.enemy.sprite.move(self.enemy.coord)
        self.coord = self.enemy.coord
            
    def avoid(self, point):
        self.enemy.avoid(point)