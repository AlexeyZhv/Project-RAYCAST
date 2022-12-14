import pygame as pg
import numpy as np
from textures import *
import ray_module as rm
from ray_module import *
from weapons import *
from Global import *
import Global as g
from Player import *
from Beam import *
from Sprites import *
from Input import *
from Widgets import *
from Enemy import *

obs = Player([130, 104], 3 * np.pi / 2, 200, 2, 24)
PISTOL = Pistol(obs)
SWORD = Sword(obs)
SHIELD = Shield(obs)
BOW = Bow(obs)
selected_weapon = 0
WEAPONS1 = [SWORD, SHIELD]
WEAPONS2 = [BOW, BOW]
WEAPONS = WEAPONS1
OBJECTS = []


Elf([896, 896])
Ork([896 - 128, 896])
Ork([128, 896])
Ork([256, 896])
Elf([64 * 6, 64 * 6])

def new_texture(size):
    a = []
    for i in range(size):
        b = []
        for j in range(size):
            b.append(0)
        a.append(b)
    return a

def distance(obj):
    return mag(obj.coord - obs.coord)

pg.init()
pg.display.set_caption("RAYCASTER")
font = pg.font.SysFont("comicsansms", 30)
pg.mouse.set_visible(False)

while not g.finished:
    trigger_pressed = False
    interacting = False
    shooting = False
    clock.tick(FPS)
    fps_label = font.render(f"FPS: {int(clock.get_fps())}", True, "RED")
    hp_label = font.render(f"HEALTH: {int(obs.hp)}", True, "RED")

    if obs.hp <= 0:
        g.DIED = True
    if len(g.ENEMIES) <= 0:
        g.VICTORY = True

    settings_menu()
    main_menu()
    pause_menu()
    die_menu()
    victory_menu()

    if len(g.ENEMIES) <= 0:
        g.game_ended = True

    #Checking main controls
    for event in pg.event.get():
        if event.type == pg.QUIT:
            g.finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_TAB:
                if WEAPONS == WEAPONS1:
                    WEAPONS = WEAPONS2
                else:
                    WEAPONS = WEAPONS1
            if event.key == pg.K_m:
                if MODE == "3D":
                    MODE = "Map"
                else:
                    MODE = "3D"
            if event.key == pg.K_e:
                interacting = True
            if event.key == pg.K_ESCAPE:
                g.PAUSED = True  
        if event.type == pg.MOUSEBUTTONDOWN:
            left, middle, right = pg.mouse.get_pressed()
            if left:
                shooting = True

    left, middle, right = pg.mouse.get_pressed()
    trigger_pressed = right

    #Changing weapons
    if WEAPONS[0].state == "ready" and trigger_pressed:
        selected_weapon = 1
    elif WEAPONS[1].state == "ready" and shooting:
        selected_weapon = 0

    if MODE == "3D":
        obs.ang += mouse_control()
        if obs.ang >= 2 * np.pi:
            obs.ang -= 2 * np.pi
        elif obs.ang < 0:
            obs.ang += 2 * np.pi


    # check if there is a wall in front of the player
    i_w = 0
    j_w = 0
    is_wall = False
    if interacting:
        if obs.ang < np.pi / 4 or obs.ang > 7 * np.pi / 4:
            i = int(obs.coord[0] // 64) + 1
            j = int(obs.coord[1] // 64)
            is_wall = Level[j][i]
        elif obs.ang < 3 * np.pi / 4:
            i = int(obs.coord[0] // 64)
            j = int(obs.coord[1] // 64) + 1
            is_wall = Level[j][i]
        elif obs.ang < 5 * np.pi / 4:
            i = int(obs.coord[0] // 64) - 1
            j = int(obs.coord[1] // 64)
            is_wall = Level[j][i]
        elif obs.ang < 7 * np.pi / 4:
            i = int(obs.coord[0] // 64)
            j = int(obs.coord[1] // 64) - 1
            is_wall = Level[j][i]
        k = i
        m = j

    # Interaction with walls
    if (is_wall > 0) and interacting and not finished:
        #Special Cases

        #Door
        if is_wall == 2:
            Level[m][k] = 0
        

        #Drawing in editor
        else:
            MODE = "Draw"
            tex = TEXTURES[is_wall]
            if is_wall < len0:
                texture = []
                for j in tex:
                    row = []
                    for i in j:
                        row.append(i)
                    texture.append(row)
            else:
                texture = tex
            tex_scale = min(height / len(texture), width / len(texture[0]))
            drawscreen = pg.surface.Surface([len(texture[0]) * tex_scale, len(texture) * tex_scale])
            COLOR = 0
            while MODE == "Draw" and not g.finished:
                chcolor = False
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        g.finished = True
                        mode = "3D"
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_TAB:
                            COLOR += 1
                            if COLOR >= len(COLORS):
                                COLOR = 0
                        if event.key == pg.K_e:
                            MODE = "3D"

                left, middle, right = pg.mouse.get_pressed()
                if left:
                    chcolor = True
                x1, y = pg.mouse.get_pos()
                x = x1 - (width - drawscreen.get_width()) / 2

                if chcolor:
                    i, j = int(x // tex_scale), int(y // tex_scale)
                    if i < 0:
                        i = 0
                    if j < 0:
                        j = 0
                    if i > len(texture[j]) - 1:
                        i = len(texture[j]) - 1
                    if j > len(texture) - 1:
                        j = len(texture) - 1
                    texture[j][i] = COLORS[COLOR]

                clock.tick(FPS)
                screen.fill("#444444")
                drawscreen.fill("#444444")
                for i in range(len(texture[0])):
                    for j in range(len(texture)):
                        pg.draw.rect(drawscreen, texture[j][i],
                                     [[tex_scale * i + 1, tex_scale * j + 1], [tex_scale - 2, tex_scale - 2]])
                screen.blit(drawscreen, [(width - drawscreen.get_width()) / 2, 0])
                pg.draw.circle(screen, "GREY", [x1, y], 7)
                pg.draw.circle(screen, COLORS[COLOR], [x1, y], 6)
                pg.display.update()
            if is_wall < len0:
                TEXTURES.append(texture)
            Level[m][k] = TEXTURES.index(texture)

    pcol = "GREEN"
    alpha, move = move_controls(obs.ang)
    for i in range(lw):
        for j in range(lw):
            if (Level[j][i] > 0) and obs.collision(i, j, alpha)[0]:
                #print(obs.collision(i, j, alpha)[0], obs.collision(i, j, alpha)[2], obs.collision(i, j, alpha)[3])
                pcol = "YELLOW"
                if obs.collision(i, j, alpha)[1]:
                    pcol = "RED"

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        obs.rotate(1)
    elif keys[pg.K_LEFT]:
        obs.rotate(-1)

    if move:
        obs.move(alpha, Level)

    if MODE == "3D":
        #Drawing floor and ceil
        screen.fill([int(38 * 1.2), int(43 * 1.2), int(68 * 1.2)])
        pg.draw.rect(screen, [int(38 * 0.6), int(43 * 0.6), int(68 * 0.6)], [[0, 0], [width, height / 2]])
    elif MODE == "Map":
        screen.fill("#444444")
        mapscreen.fill("#444444")
        for i in range(lw):
            for j in range(lw):
                if Level[j][i] == 0:
                    pg.draw.rect(mapscreen, colors[0], [[64 * mapscale * i + 1, 64 * mapscale * j + 1],
                                                        [64 * mapscale - 2, 64 * mapscale - 2]])
                else:
                    pg.draw.rect(mapscreen, colors[1], [[64 * mapscale * i + 1, 64 * mapscale * j + 1],
                                                        [64 * mapscale - 2, 64 * mapscale - 2]])

    # RAYCASTING
    for offset in np.linspace(- fov_rad / 2, fov_rad / 2, g.rays_number):
        angle = offset + obs.ang
        if angle > 2 * np.pi:
            angle -= 2 * np.pi
        elif angle < 0:
            angle += 2 * np.pi
        # Calculating ray props
        hor_vec, ver_vec, hor_cell, ver_cell = rm.ray(Level, obs.coord, angle)
        # Walls
        if mag(ver_vec) > mag(hor_vec):
            if MODE == "Map":
                pg.draw.line(mapscreen, "#004400", obs.coord * mapscale, (obs.coord + hor_vec) * mapscale)
            elif MODE == "3D":
                texdraw(screen, hor_cell[1], TEXTURES[hor_cell[0]], wall_height / mag(hor_vec) / np.cos(offset) * scale,
                        [(offset + fov_rad / 2) * scale, height / 2], int(width / g.rays_number) + 1, 0)
        else:
            if MODE == "Map":
                pg.draw.line(mapscreen, "#003300", obs.coord * mapscale, (obs.coord + ver_vec) * mapscale)
            elif MODE == "3D":
                texdraw(screen, ver_cell[1], TEXTURES[ver_cell[0]], wall_height / mag(ver_vec) / np.cos(offset) * scale,
                        [(offset + fov_rad / 2) * scale, height / 2], int(width / g.rays_number) + 1, 0.3)

    # Shooting weapons
    if MODE == "3D":
        WEAPONS[selected_weapon].shoot(Level)
    
    ENEMIES.sort(key=distance, reverse=False)
    if MODE == "Map":
        pg.draw.circle(mapscreen, pcol, obs.coord * mapscale, 5)

        for enemy in ENEMIES:
            pg.draw.circle(mapscreen, "BLUE", enemy.coord * mapscale, 5)

        screen.blit(mapscreen, [0.5 * (width - height), 0])


    elif MODE == "3D":
        for beam in BEAMS:
            beam.draw(obs, screen)
        for enemy in ENEMIES:
            for ray in RAYS:
                if ray.check_intersection_with_enemy(enemy):
                    enemy.hp = enemy.hp - 1
                RAYS.remove(ray)
                del ray

    # enemy movement
    for enemy in ENEMIES:
        enemy.move(obs, Level)
        for enemy2 in ENEMIES:
            if enemy != enemy2 and mag(enemy.coord - enemy2.coord) <= 30:
                enemy.avoid(enemy2.coord)

    screen.blit(fps_label, [hp_label.get_width() / 2, 20])
    screen.blit(hp_label, [width - 1.5 * hp_label.get_width(), 20])

    for bullet in BULLETS:
        bullet.update()

    #testing drawings
    OBJECTS = ENEMIES + LAMPS + BULLETS + EXPLOSIONS
    OBJECTS.sort(key=distance, reverse=True)
    if MODE == "3D":
        for obj in OBJECTS:
            obj.draw(Level, obs, screen)
        WEAPONS[selected_weapon].draw(screen, shooting, trigger_pressed)

    #screen.blit(swordsman_idle_surface, [0, 0])
    screen.blit(grad_surf, [0, 0])
    pg.display.update()

pg.quit()
