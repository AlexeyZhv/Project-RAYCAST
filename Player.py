from Global import *
from Math.Vector import *


class Player:
    def __init__(self, coord, ang, spd, omega, size):
        self.size = [size]
        self.coord = np.array(coord)
        self.ang = ang
        self.spd = spd
        self.omega = omega
        self.hp = 10
        self.is_ver_wall_collision = False
        self.is_hor_wall_collision = False

    def move(self, angle):
        self.coord = self.coord + self.spd / FPS * rotate([1, 0], angle)
        if self.is_ver_wall_collision:
            self.coord[0] - self.spd[0] / FPS
        if self.is_hor_wall_collision:
            self.coord[1] - self.spd[1] / FPS
        self.is_ver_wall_collision = False
        self.is_hor_wall_collision = False

    def rotate(self, dirc):
        self.ang += dirc / FPS * self.omega
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi

    def collision(self, i, j, angle):
        shift = rotate([2 * self.spd / FPS, 0], angle)
        ver_collision = (
                        self.coord[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                        self.coord[0] >= 64 * i - 2 * self.spd / FPS)
        hor_collision = (
                        self.coord[1] >= 64 * j - 2 * self.spd / FPS) and (
                        self.coord[1] <= 64 * (j + 1) + 2 * self.spd / FPS)
        if ver_collision:
            self.is_ver_wall_collision = True
        if hor_collision:
            self.is_hor_wall_collision = True
        return [
            ver_collision and hor_collision,
            (self.coord[0] + shift[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                        self.coord[0] + shift[0] >= 64 * i - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] >= 64 * j - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] <= 64 * (j + 1) + 2 * self.spd / FPS)
        ]

    def increase_ang(self, value):
        self.ang += value
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi
