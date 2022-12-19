import pygame as pg
import numpy as np
import textures
from textures import *

width = 1200
height = 800
screen = pg.display.set_mode([width, height])
mapscreen = pg.surface.Surface([height, height])
drawscreen = pg.surface.Surface([height, height])
FPS = 60
FOV = 60
rays_number = 100
fov_rad = FOV * np.pi / 180
scale = width / fov_rad
wall_height = 48
colors = ["BLACK", "WHITE", "GREEN", "RED", "RED", "WHITE", "BLUE", "GREEN"]


MODE = "3D"
len0 = len(TEXTURES)
BEAMS = []
RAYS = []
EXPLOSIONS = []
BULLETS = []

SETTINGS = False
PAUSED = False
MENU = True

BULLET_DAMAGE = 1

fireball = pg.image.load("./sprites/fireball.png")
ohno = pg.image.load("./sprites/ohno.png")
target = pg.image.load("./sprites/target.png")
ork = pg.image.load("./sprites/enemies/ork.png")
grad = pg.image.load("./sprites/grad.png")
grad_surf = pg.surface.Surface(grad.get_size(), pg.SRCALPHA)
grad_surf.blit(grad, [0, 0])

finished = False
clock = pg.time.Clock()

Level = [  # Square only
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4],
    [4, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4],
    [4, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4],
    [4, 0, 0, 4, 4, 4, 0, 4, 4, 0, 0, 4, 4, 4, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 2, 2, 0, 4, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 4, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 0, 0, 4, 4, 4, 6, 4, 4, 4, 0, 4, 4],
    [4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4],
    [4, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4],
    [4, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0, 4, 0, 0, 0, 4],
    [4, 0, 0, 4, 4, 4, 0, 4, 4, 0, 0, 4, 4, 4, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]

lw = len(Level)
mapscale = (height / (lw * 64))

#Enemies list
ENEMIES = []

# methods

def rotate(vec, ang):
    return np.dot(vec, [[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])


def mag(vec):
    return np.sqrt(np.sum(index ** 2 for index in vec))


def transform(c_0, vec, coord):
    x, y = vec[0], vec[1]
    return 1 / np.sqrt(x ** 2 + y ** 2) * np.dot((np.array(coord) - np.array(c_0)), np.array([np.array([x, -y]), np.array([y, x])]))

