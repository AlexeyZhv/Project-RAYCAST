import pygame as pg
import matplotlib.image as img
import numpy as np


COLORS = [
    [0, 0, 0],
    [200, 200, 200],
    [100, 0, 0],
    [0, 100, 0],
    [0, 0, 100]
]

def read_image(path):
    texture_array = []
    im = img.imread(path)
    for j in range(len(im)):
        row_array = []
        for i in range(len(im[j])):
            r, g, b, = im[j][i][0], im[j][i][1], im[j][i][2]
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            row_array.append([r, g, b])
        texture_array.append(row_array)
    return texture_array

def texdraw(surface, intersection_coord, texture, height, coord, width, shade):
    column = int(intersection_coord / 64 * len(texture[0]))
    for row in range(len(texture)):
        x = coord[0]
        y1 = coord[1] + height * (- 0.5 + row / len(texture))
        y2 = coord[1] + height * (- 0.5 + (row + 1) / len(texture))
        col1 = texture[row][column]
        col = []
        for i in range (len(col1)):
            col.append(int(col1[i] * (1 - shade)))
        pg.draw.line(surface, col, [x, y1], [x, y2], width)
    
void_texture = [[[0, 0, 0]]]
TEXTURES = [void_texture, read_image("./sprites/wall/wall.png"), read_image("./sprites/wall/wall.png")]
