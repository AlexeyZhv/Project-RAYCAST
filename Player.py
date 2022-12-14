from Global import *
from Math.Vector import *


class Player:
    def __init__(self, coord, ang, spd, omega, size):
        self.SHIELDED = False
        self.size = [size]
        self.coord = np.array(coord)
        self.ang = ang
        self.spd = spd
        self.omega = omega
        self.hp = 10
        self.vector_spd = Vector([1, 1]).set_by_angle(ang).multiply_by_number(spd)
        self.is_ver_wall_collision = False
        self.is_hor_wall_collision = False
        self.i = self.coord[0] // 64
        self.j = self.coord[1] // 64
        self.coord_inside = [self.coord[0] % 64, self.coord[1] % 64]

    def move(self, angle, lmap):
        self.coord = self.coord + self.spd / FPS * rotate([1, 0], angle)

        self.i = int(self.coord[0] / 64)
        self.j = int(self.coord[1] / 64)
        
        i1 = int((self.coord[0] - 2 * self.spd / FPS) / 64)
        i2 = int((self.coord[0] - 2 * self.spd / FPS) / 64)
        i3 = int((self.coord[0] + 2 * self.spd / FPS) / 64)
        i4 = int((self.coord[0] + 2 * self.spd / FPS) / 64)
        j1 = int((self.coord[1] - 2 * self.spd / FPS) / 64)
        j2 = int((self.coord[1] + 2 * self.spd / FPS) / 64)
        j3 = int((self.coord[1] - 2 * self.spd / FPS) / 64)
        j4 = int((self.coord[1] + 2 * self.spd / FPS) / 64)

        checksum = round(np.sign(Level[j1][i1]) + np.sign(Level[j2][i2]) + np.sign(Level[j3][i3]) + np.sign(Level[j4][i4]))

        self.coord_inside = [self.coord[0] % 64, self.coord[1] % 64]

        self.vector_spd = self.vector_spd.set_by_angle(self.ang).multiply_by_number(self.spd)

        self.is_ver_wall_collision = False
        self.is_hor_wall_collision = False
        cols = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]

        if self.j > 0:
            if Level[int(self.j - 1)][int(self.i)] > 0:
                cols[0] = self.collision(self.i, self.j - 1, self.ang)
                cols[0][2] = False
        if self.i < len(Level) - 1:
            if Level[int(self.j)][int(self.i + 1)] > 0:
                cols[1] = self.collision(self.i + 1, self.j, self.ang)
                cols[1][3] = False
        if self.j < len(Level) - 1:
            if Level[int(self.j + 1)][int(self.i)] > 0:
                cols[2] = self.collision(self.i, self.j + 1, self.ang)
                cols[2][2] = False
        if self.i > 0:
            if Level[int(self.j)][int(self.i - 1)] > 0:
                cols[3] = self.collision(self.i - 1, self.j, self.ang)
                cols[3][3] = False

        for col in cols:
            if col[2]:
                self.is_ver_wall_collision = True
            if col[3]:
                self.is_hor_wall_collision = True

        if self.is_ver_wall_collision or checksum == 1 or checksum == 3:
            if self.coord_inside[0] <= 2 * self.spd / FPS:
                self.coord[0] = 64 * self.i + 2 * self.spd / FPS
            else:
                self.coord[0] = 64 * (self.i + 1) - 2 * self.spd / FPS
        if self.is_hor_wall_collision:
            if self.coord_inside[1] <= 2 * self.spd / FPS:
                self.coord[1] = 64 * self.j + 2 * self.spd / FPS
            else:
                self.coord[1] = 64 * (self.j + 1) - 2 * self.spd / FPS



    def rotate(self, dirc):
        self.ang += dirc / FPS * self.omega
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi

    def collision(self, i, j, angle):
        shift = rotate([2 * self.spd / FPS, 0], angle)
        col = (
                (self.coord[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                    self.coord[0] >= 64 * i - 2 * self.spd / FPS) and
            (
                    self.coord[1] >= 64 * j - 2 * self.spd / FPS) and (
                    self.coord[1] <= 64 * (j + 1) + 2 * self.spd / FPS))

        return [
            col,
            (self.coord[0] + shift[0] <= 64 * (i + 1) + 2 * self.spd / FPS) and (
                        self.coord[0] + shift[0] >= 64 * i - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] >= 64 * j - 2 * self.spd / FPS) and (
                        self.coord[1] + shift[1] <= 64 * (j + 1) + 2 * self.spd / FPS),
            ((
                    64 * (i + 1) + 2 * self.spd / FPS >= self.coord[0] >= 64 * (i + 1) - 2 * self.spd / FPS
            ) or
            (
                    64 * i + 2 * self.spd / FPS >= self.coord[0] >= 64 * i - 2 * self.spd / FPS
            )) and col,
            ((
                    64 * (j + 1) + 2 * self.spd / FPS >= self.coord[1] >= 64 * (j + 1) - 2 * self.spd / FPS
            ) or
            (
                    64 * j + 2 * self.spd / FPS >= self.coord[1] >= 64 * j - 2 * self.spd / FPS
            )) and col

        ]

    def increase_ang(self, value):
        self.ang += value
        if self.ang > 2 * np.pi:
            self.ang -= 2 * np.pi
        elif self.ang < 0:
            self.ang += 2 * np.pi
