import numpy as np
import pygame as pg
from ray_module import *
from Global import *

class Sprite:
    def __init__(self, coord, texture, size, qual):
        self.coord = np.array(coord)
        self.qual = qual
        self.size = np.array(size)
        #splitting image into columns
        step = texture.get_width() / (self.qual - 1)
        self.columns = []
        for i in range(self.qual - 1)[::-1]:
            temp_surface = pg.Surface((texture.get_width() / (self.qual - 1), texture.get_height()), pg.SRCALPHA)
            temp_surface.blit(texture, [- i * step, 0])
            self.columns.append(temp_surface)

    def draw(self, lmap, player, surface):
        dist = mag([self.coord[1] - player.coord[1], self.coord[0] - player.coord[0]])
        step = self.size[0] / (self.qual - 1)
        offsets = []
        dists = []
        visible = []
        if dist > 20:
            #calculating angles
            ang = np.arctan2(self.coord[1] - player.coord[1], self.coord[0] - player.coord[0])
            angsize = self.size / dist * scale
            if ang < 0:
                ang += 2 * np.pi
            #rotating sprite, calculating props
            for i in range(self.qual):
                coord = self.coord + rotate([0, self.size[0] / 2 - i * step], ang)
                angle = np.arctan2(coord[1] - player.coord[1], coord[0] - player.coord[0])
                distance = mag([coord[1] - player.coord[1], coord[0] - player.coord[0]])
                if angle < 0:
                    angle += 2 * np.pi
                hor_vec, ver_vec, hor_cell, ver_cell = ray(lmap, player.coord, angle)
                visible.append(dist <= mag(hor_vec) and dist <= mag(ver_vec))
                offset = angle - player.ang
                if offset > np.pi:
                    offset -= 2 * np.pi
                elif offset < - np.pi:
                    offset += 2 * np.pi
                offsets.append(offset)
                dists.append(distance)
            #displaying the columns
            if len(offsets) > 1:
                for i in range(len(offsets) - 1):
                    if abs(offsets[i] - offsets[i + 1]) < np.pi:
                        dist = (dists[i] + dists[i + 1]) / 2
                        wid = abs(offsets[i] - offsets[i + 1])
                        if visible[i] and visible[i + 1]:
                            surface.blit(pg.transform.scale(self.columns[i], [wid * scale + 1, angsize[1]]), [offsets[i + 1] * scale + width / 2, height / 2 - angsize[1] / 2])
