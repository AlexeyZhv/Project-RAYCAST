from Global import *
import Global as g
from Math.Vector import *
from Math.Ray import *
from ray_module import ray
from Sprites import * 
from Beam import *

class Bullet:
    def __init__(self, start_coord, direction, speed, player, source="enemy"):
        self.velocity = direction.multiply_by_number(speed / direction.length)
        self.start_coord = np.array(start_coord)
        self.coord = np.array(start_coord)
        self.prev_coord = self.coord

        #raycasting
        hor_vec, ver_vec, trash, trash = ray(Level, self.coord, self.velocity.convert_to_angle())
        self.final_coord = self.coord + min([hor_vec, ver_vec], key=mag)
        self.trajectory_vector = Vector(self.final_coord - self.start_coord)

        self.enemy = None
        self.sprite = Sprite(self.coord, fireball, [12, 48], 3, 50)
        self.hitscan = Hitscan(self.coord, self.trajectory_vector, self.trajectory_vector.length, Level)
        self.player = player
        self.source = source
        g.BULLETS.append(self)

    def update(self):
        self.prev_coord = np.array(list(self.coord))
        self.coord[0] += self.velocity.x / FPS
        self.coord[1] += self.velocity.y / FPS
        self.sprite.move(self.coord)

        if self.source == "enemy":
            if self.check_player_collision(self.player):
                self.player.hp -= BULLET_DAMAGE
                g.BULLETS.remove(self)
                del self
                return

        if self.check_enemy_collision():
            if self.source == "player":
                self.enemy.hp -= BULLET_DAMAGE
            expl(self.prev_coord)
            g.BULLETS.remove(self)
            del self
            return
            
        elif Vector(self.coord - self.start_coord).length >= self.trajectory_vector.length:
            expl(self.prev_coord)
            g.BULLETS.remove(self)
            del self
            return


    def check_enemy_collision(self):
        hit = False
        for enemy in g.ENEMIES:
            hitscan = Hitscan(self.prev_coord, self.trajectory_vector, mag(self.coord - self.prev_coord) + enemy.size[0]/4, Level)
            hit = hitscan.check_intersection_with_enemy(enemy)
            del hitscan
            if hit:
                self.enemy = enemy
                return True
        if not hit:
            return False
    
    def check_player_collision(self, player):
        hitscan = Hitscan(self.prev_coord, self.trajectory_vector, mag(self.coord - self.prev_coord) + player.size[0]/4, Level)
        hit = hitscan.check_intersection_with_enemy(player)
        del hitscan
        if hit:
            self.player = player
            return True
        else:
            return False

class Elf_arrow(Bullet):
    def __init__(self, start_coord, direction, speed, player):
        super().__init__(start_coord, direction, speed, player, "enemy")
        self.sprite = Sprite(self.coord, arrow, [3, 48], 2, 50)
    
    def draw(self, lmap, player, surface):
        Beam(lmap, self.coord, self.velocity.convert_to_angle(), mag(self.coord - self.prev_coord), 0, 500, 2, 0.1)
        self.sprite.draw(lmap, player, surface)

class Fireball(Bullet):
    def __init__(self, start_coord, direction, speed, player):
        super().__init__(start_coord, direction, speed, player, "player")
        self.sprite = Sprite(self.coord, fireball, [12, 48], 2, 50)
    
    def draw(self, lmap, player, surface):
        self.sprite.draw(lmap, player, surface)
