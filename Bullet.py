from Global import *
import Global as g
from Math.Vector import *
from Math.Ray import *
from ray_module import ray
from Sprites import * 
from Beam import *

class Bullet:
    def __init__(self, start_coord, velocity):
        self.velocity = velocity
        self.start_coord = np.array(start_coord)
        self.coord = np.array(start_coord)
        self.prev_coord = self.coord
        hor_vec, ver_vec, trash, trash = ray(Level, self.coord, self.velocity.convert_to_angle())
        self.final_coord = self.coord + min([hor_vec, ver_vec], key=mag)
        self.trajectory_vector = Vector(self.final_coord - self.start_coord)
        self.enemy = None
        self.sprite = Sprite(self.coord, fireball, [12, 48], 3, 50)
        self.hitscan = Hitscan(self.coord, self.trajectory_vector, self.trajectory_vector.length, Level)
        g.BULLETS.append(self)

    def draw(self, lmap, player, surface):
        self.sprite.draw(lmap, player, surface)

    def update(self):
        self.prev_coord = self.coord
        self.coord[0] += self.velocity.x / FPS
        self.coord[1] += self.velocity.y / FPS
        self.sprite.move(self.coord)
        if Vector(self.coord - self.start_coord).length >= self.trajectory_vector.length:
            expl(self.prev_coord)
            g.BULLETS.remove(self)
            del self
        elif self.check_enemy_collision():
            self.enemy.health -= BULLET_DAMAGE
            expl(self.prev_coord)
            g.BULLETS.remove(self)
            del self

    def check_enemy_collision(self):
        hit = False
        for enemy in g.ENEMIES:
            hitscan = Hitscan(self.prev_coord, self.trajectory_vector, mag(self.coord - self.prev_coord) + enemy.size[0]/4, Level)
            hit = hitscan.check_intersection_with_enemy(enemy)
            if hit:
                self.enemy = enemy
                return True
        if not hit:
            return False


