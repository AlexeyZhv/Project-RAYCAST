import numpy as np

from Global import *
from Math.Vector import *
from ray_module import *


class Hitscan:
    def __init__(self, pos, vector, length, lmap):
        self.pos = np.array(pos)
        self.vector = vector.multiply_by_number(1 / vector.length)
        self.length = length
        ang = self.vector.convert_to_angle()
        hor_vec, ver_vec, hor_cell, ver_cell = ray(lmap, self.pos, ang)
        self.length = min(length, min(mag(hor_vec), mag(ver_vec)))
        RAYS.append(self)

    def check_intersection_with_enemy(self, enemy):
        enemy_vector = Vector(enemy.coord - self.pos)
        enemy_dist_sq = (enemy_vector.length ** 2 - enemy_vector.projection(self).length ** 2)
        if self.vector.scalar_product(enemy_vector) > 0 and enemy_dist_sq < (enemy.size[0] / 2) ** 2 and enemy_vector.length <= self.length:
            return True
        else:
            return False


