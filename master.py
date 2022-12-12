import pygame as pg
import numpy as np
from textures import *
from ray_module import *
from weapons import *
from Global import *
import Global
from Player import *
from Beam import *
from Sprites import *
from Input import *
from Widgets import *

from random import random

oh_no = Sprite([896, 896], ohno, [48, 48], 9, 10)
Shotgun = Weapon()

obs = Player([104, 104], 3 * np.pi / 2, 200, 3)

def new_texture(size):
    a = []
    for i in range(size):
        b = []
        for j in range(size):
            b.append(0)
        a.append(b)
    return a

pg.init()
pg.display.set_caption("RAYCASTER")
font = pg.font.SysFont("comicsansms", 30)
pg.mouse.set_visible(False)

while not Global.finished:
    interacting = False
    shooting = False
    clock.tick(FPS)
    fps_label = font.render(f"FPS: {int(clock.get_fps())}", True, "RED")

    main_menu()
    pause_menu()

    #Checking main controls
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Global.finished = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_TAB:
                if MODE == "3D":
                    MODE = "Map"
                else:
                    MODE = "3D"
            if event.key == pg.K_e:
                interacting = True
            if event.key == pg.K_ESCAPE:
                Global.PAUSED = True
            if event.key == pg.K_SPACE:
                shooting = True

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
            tex_scale = height / len(texture)
            COLOR = 0
            while MODE == "Draw":
                chcolor = False
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        finished = True
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
                x = x1 - (width / 2 - height / 2)

                if chcolor:
                    i, j = int(x // tex_scale), int(y // tex_scale)
                    if i < 0:
                        i = 0
                    if j < 0:
                        j = 0
                    if i > len(texture) - 1:
                        i = len(texture) - 1
                    if j > len(texture) - 1:
                        j = len(texture) - 1
                    texture[j][i] = COLOR

                clock.tick(FPS)
                screen.fill("#444444")
                drawscreen.fill("#444444")
                for i in range(len(texture)):
                    for j in range(len(texture[0])):
                        pg.draw.rect(drawscreen, COLORS[texture[j][i]],
                                     [[tex_scale * i + 1, tex_scale * j + 1], [tex_scale - 2, tex_scale - 2]])
                screen.blit(drawscreen, [(width - height) / 2, 0])
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
                pcol = "YELLOW"
                if obs.collision(i, j, alpha)[1]:
                    move = False
                    pcol = "RED"

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        obs.rotate(1)
    elif keys[pg.K_LEFT]:
        obs.rotate(-1)

    if move:
        obs.move(alpha)

    if MODE == "3D":
        #Floor and ceil
        screen.fill("#222222")
        pg.draw.rect(screen, "#666666", [[0, 0], [width, height / 2]])
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
    for offset in np.linspace(- fov_rad / 2, fov_rad / 2, rays_number):
        angle = offset + obs.ang
        if angle > 2 * np.pi:
            angle -= 2 * np.pi
        elif angle < 0:
            angle += 2 * np.pi
        # Calculating ray props
        hor_vec, ver_vec, hor_cell, ver_cell = ray(Level, obs.coord, angle)
        # Walls
        if mag(ver_vec) > mag(hor_vec):
            if MODE == "Map":
                pg.draw.line(mapscreen, "#004400", obs.coord * mapscale, (obs.coord + hor_vec) * mapscale)
            elif MODE == "3D":
                texdraw(screen, hor_cell[1], TEXTURES[hor_cell[0]], wall_height / mag(hor_vec) / np.cos(offset) * scale,
                        [(offset + fov_rad / 2) * scale, height / 2], int(width / rays_number) + 1, 0)
        else:
            if MODE == "Map":
                pg.draw.line(mapscreen, "#003300", obs.coord * mapscale, (obs.coord + ver_vec) * mapscale)
            elif MODE == "3D":
                texdraw(screen, ver_cell[1], TEXTURES[ver_cell[0]], wall_height / mag(ver_vec) / np.cos(offset) * scale,
                        [(offset + fov_rad / 2) * scale, height / 2], int(width / rays_number) + 1, 0.5)

    # Code for the laser shotgun
    if MODE == "3D":
        if Shotgun.state == 1:
            for i in range(5):
                BEAMS.append(Beam(
                    Level, [obs.coord[0] + 15 * np.cos(obs.ang), obs.coord[1] + 15 * np.sin(obs.ang)],
                    obs.ang + (0.5 - random()) * 0.3, 300, 3, 500, 10
                ))
    if MODE == "Map":
        pg.draw.circle(mapscreen, pcol, obs.coord * mapscale, 5)
        screen.blit(mapscreen, [0.5 * (width - height), 0])
    elif MODE == "3D":
        for beam in BEAMS:
            beam.draw(obs, screen)
    screen.blit(fps_label, [20, 20])
    for beam in BEAMS:
        if beam.timer > 0.2:
            BEAMS.remove(beam)
            del beam

    #testing drawings
    if MODE == "3D":
        for lamp in LAMPS:
            lamp.draw(Level, obs, screen)
        Shotgun.draw(screen, shooting)

    pg.display.update()

pg.quit()
