import pygame as pg
import numpy as np
from textures import *
from ray_module import *
from weapons import *
from Global import *
from Player import *
from Sprites import *
from Beam import *

elf_reload = 2

ork_run = []
for i in range(8):
    sprite = pg.image.load(f"./sprites/enemies/ork_run/ork_run_{i}.png")
    ork_run.append(sprite)

ork_attack = []
for i in range(8):
    sprite = pg.image.load(f"./sprites/enemies/ork_attack/ork_attack_{i}.png")
    ork_attack.append(sprite)

elf_run = []
for i in range(8):
    sprite = pg.image.load(f"./sprites/enemies/elf_run/elf_run_{i}.png")
    elf_run .append(sprite)

elf_attack = []
for i in range(12):
    sprite = pg.image.load(f"./sprites/enemies/elf_attack/elf_attack_{i}.png")
    elf_attack.append(sprite)

class Enemy:
    def __init__(self, coord, size, spd, hp=1, texture=ohno):
        self.coord = np.array(coord)
        self.size = size
        self.spd = spd
        self.sprite = Sprite(self.coord, texture, self.size, 5, 20)
        self.hp = hp
        self.mem = self.coord
        self.timer = 0
        ENEMIES.append(self)

    '''def __del__(self):
        expl(self.coord)'''

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
        super().__init__(coord, [48, 48], 100, 2, ork)
        self.state = "running"
        self.attacked = False
    
    def draw(self, lmap, player, surface):

        if self.state == "running":
            self.timer += 1 / FPS
            if self.timer >= 0.8:
                self.timer = 0
            self.sprite = Sprite(self.coord, ork_run[int(self.timer / 0.1)], self.size, 5, 20)
            self.sprite.draw(lmap, player, surface)

        elif self.state == "attacking":
            self.timer += 1 / FPS
            if self.timer >= 0.8:
                self.timer = 0
                self.attacked = False
            self.sprite = Sprite(self.coord, ork_attack[int(self.timer / 0.1)], self.size, 5, 20)
            self.sprite.draw(lmap, player, surface)

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

        #checking states
        if self.state == "running" and vect.length < 40 and is_mem == 0:
            self.state = "attacking"
            self.attacked = False
            self.timer = 0
        elif self.state == "attacking" and vect.length > 64 or is_mem == 1:
            self.state = "running"
            self.attacked = False
            self.timer = 0

        if (vect.length > 40 or is_mem == 1) and vect.length > 5 and self.state == "running":
            vect = vect.multiply_by_number(self.spd / FPS / vect.length)
            vect_arr = np.array([vect.x, vect.y])
            self.coord = self.coord + vect_arr
            self.sprite.move(self.coord)

        self.attack(player, level_map)

        if self.hp <= 0:
            g.ENEMIES.remove(self)
            del self

    def attack(self, player, lmap):
        if self.state == "attacking" and not self.attacked:
            if self.timer > 0.1:
                self.attacked = True
                player.hp -= 1


class Elf(Enemy):

    def __init__(self, coord):
        super().__init__(coord, [24, 48], 200, 1)
        self.charge = 0
        self.timer = 0
        self.state = "running"

    def draw(self, lmap, player, surface):
        if self.state == "running":
            self.timer += 1 / FPS
            if self.timer >= 0.8:
                self.timer = 0
            self.sprite = Sprite(self.coord, elf_run[int(self.timer / 0.1)], self.size, 5, 20)
            self.sprite.draw(lmap, player, surface)

        elif self.state == "attacking":
            self.timer += 1 / FPS
            if self.timer >= elf_reload:
                self.timer = 0
                self.attacked = False
            if self.timer < 1.2:
                self.sprite = Sprite(self.coord, elf_attack[int(self.timer / 0.1)], self.size, 5, 20)
            else:
                self.sprite = Sprite(self.coord, elf_attack[0], self.size, 5, 20)
            self.sprite.draw(lmap, player, surface)

    def move(self, player, lmap):
        '''
        if enemy sees player, he will move to player, else he will move to last player's posintion
        :param player:
        :param level_map:
        :return:
        '''
        vect = Vector(player.coord - self.coord)
        length = vect.length
        hor_vec, ver_vec, trash, trash = ray(lmap, self.coord, vect.convert_to_angle())

        l_new = min(mag(hor_vec), mag(ver_vec))

        is_mem = 0
        if (l_new >= length):
            self.mem = player.coord
        else:
            vect = Vector(self.mem - self.coord)
            is_mem = 1

        #checking states
        if self.state == "running" and vect.length < 500 and is_mem == 0:
            self.state = "attacking"
            self.attacked = False
            self.timer = 0
        elif self.state == "attacking" and vect.length > 600 or is_mem == 1:
            self.state = "running"
            self.attacked = False
            self.timer = 0

        if (vect.length > 500 or is_mem == 1) and vect.length > 200 and self.state == "running":
            vect = vect.multiply_by_number(self.spd / FPS / vect.length)
            vect_arr = np.array([vect.x, vect.y])
            self.coord = self.coord + vect_arr
            self.sprite.move(self.coord)

        self.attack(player, lmap)
        if self.hp <= 0:
            g.ENEMIES.remove(self)
            del self

    def attack(self, player, lmap):
        enemy_vect_list = list(player.coord - self.coord)
        enemy_vect = Vector(enemy_vect_list)
        coord = self.coord + rotate([4, 0], enemy_vect.convert_to_angle() + np.pi / 2.1)
        vect_list = list(player.coord - coord)
        vect = Vector(vect_list)

        hor_vec, ver_vec, trash, trash = ray(lmap, self.coord, vect.convert_to_angle())
        vec = min([hor_vec, ver_vec], key=mag)
        l_ray = mag(vec)
        if vect.length < l_ray:
            if self.state == "attacking" and not self.attacked:
                if self.timer > 0.7:
                    self.attacked = True
                    Elf_arrow(player.coord - np.array(vect_list), vect, 1000, player) 
        else:
            self.timer = 0

