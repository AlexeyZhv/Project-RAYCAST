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
    def __init__(self, pos, size):
        self.pos = np.array(pos)
        self.size = size
        self.sprite = Sprite(self.pos, ohno, self.size, 5, 20)
        self.health = 1
        ENEMIES.append(self)

    def draw(self, lmap, player, surface):
        self.sprite.draw(lmap, player, surface)



