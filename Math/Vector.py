import numpy as np

from Global import *


class Vector:
    def __init__(self, pos):
        self.x = np.array(pos)[0]
        self.y = np.array(pos)[1]
        self.length = (self.x ** 2 + self.y ** 2) ** 0.5

    def add(self, vector):
        return Vector([self.x + vector.x, self.y + vector.y])

    def multiply_by_number(self, k):
        return Vector([self.x * k, self.y * k])

    def scalar_product(self, vector):
        return self.x * vector.x + self.y * vector.y

    def projection(self, ray):
        return ray.vector.multiply_by_number(self.scalar_product(ray.vector))
    
    def vec_projection(self, vector):
        return vector.multiply_by_number(self.scalar_product(vector))

    def is_collinear(self, vector):
        return self.x * vector.y == self.y * vector.x

    def is_co_directed(self, vector):
        if self.length == 0:
            return True
        if vector.length == 0:
            return True
        return self.is_collinear(vector) and (self.x * vector.x > 0 or self.y * vector.y > 0)

    def is_opposite_directed(self, vector):
        if self.length == 0:
            return True
        if vector.length == 0:
            return True
        return self.is_collinear(vector) and (self.x * vector.x < 0 or self.y * vector.y < 0)

    def convert_to_angle(self):
        alpha = np.arctan2(self.y, self.x)
        if alpha < 0:
            alpha += 2 * np.pi
        elif alpha > 2 * np.pi:
            alpha -= 2 * np.pi
        return alpha

    def set_by_angle(self, angle):
        self.x = np.cos(angle)
        self.y = np.sin(angle)
        return self
