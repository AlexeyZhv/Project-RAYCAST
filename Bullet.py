from Global import *
from Math.Vector import *
from ray_module import ray


class Bullet:
    def __init__(self, start_coord, velocity):
        self.velocity = velocity
        self.start_coord = start_coord
        self.coord = start_coord
        hor_vec, ver_vec, trash, trash = ray(Level, self.coord, vector.convert_to_angle())
        self.final_coord = self.coord + min([hor_vec, ver_vec], key=mag)
        self.trajectory_vector = Vector(self.final_coord - self.start_coord)
        self.enemy = None

    def draw(self):
        #Draw Bullet
        None

    def update(self):
        self.coord[0] += velocity.x
        self.coord[1] += velocity.y
        if Vector(self.coord - self.start_coord).length >= self.trajectory_vector:
            del self
        if self.check_enemy_collision():
            self.enemy.health -= BULLET_DAMAGE
            del self

    def check_enemy_collision(self):
        for enemy in ENEMIES:
            enemy_vector = Vector(enemy.coord - self.coord)
            enemy_dist_sq = (enemy_vector.length ** 2 - enemy_vector.projection(self).length ** 2)
            if self.vector.scalar_product(enemy_vector) > 0 and enemy_dist_sq < (
                    enemy.size[0] / 2) ** 2:
                self.enemy = enemy
                return True
        return False

    def __del__(self):
        expl(self.coord)

