import pygame as pg


COLORS = [
    [0, 0, 0],
    [200, 200, 200],
    [100, 0, 0],
    [0, 100, 0],
    [0, 0, 100], 
    [0, 100, 100], 
    [200, 200, 0],
    [60, 60, 60]
]

def texdraw(surface, intersection_coord, texture, height, coord, width, shade):
    column = int(intersection_coord / 64 * len(texture[0]))
    for row in range(len(texture)):
        x = coord[0]
        y1 = coord[1] + height * (- 0.5 + row / len(texture))
        y2 = coord[1] + height * (- 0.5 + (row + 1) / len(texture))
        col1 = COLORS[texture[row][column]]
        col = []
        for i in range (len(col1)):
            col.append(int(col1[i] * (1 - shade)))
        pg.draw.line(surface, col, [x, y1], [x, y2], width)
    

texture0 = [[0]]

#Basic wall
texture1 = [
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4],       
    [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4]        
]

#DOOR
texture2 = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 7, 0, 6, 6, 0, 7, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 7, 0, 6, 6, 0, 7, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6, 6, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 6],       
    [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],       
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]        
]

#ФОПФ
texture3 =  [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4, 4, 1, 1, 1, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 1, 4, 4, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 4, 1, 1, 4, 1, 1, 1, 4, 1, 1, 4, 4, 1, 1, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 4, 1, 1, 4, 1, 1, 1, 4, 1, 1, 4, 1, 4, 1, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 4, 4, 4, 4, 4, 1, 4, 1, 4, 1, 4, 4, 4, 4, 4, 4, 1, 1, 4, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 4, 4, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

texture4 = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 4, 4, 6, 6, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 6, 6, 4, 4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 6, 6, 4, 4, 6, 6, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 6, 6, 6, 6, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 4, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 4, 4, 4, 4, 6, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5],
    [4, 6, 6, 4, 4, 6, 6, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 6, 6, 6, 6, 6, 6, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 4, 4, 6, 6, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4]
    ]

#Russia
texture5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ]

#Дельта альфа альфа штрих
texture6 = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 1, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 1, 1, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2],       
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]        
]

#Пустая текстура 32х32
texture = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

TEXTURES = [texture0, texture1, texture2, texture3, texture4, texture5, texture6]

if __name__ == "__main__":
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode([800, 800])
    texscreen = pg.surface.Surface([800, 800])
    texscale = min(800 / len(texture), 800 / len(texture[0]))
    running = True
    FPS = 60
    COLOR = 0
    while running:
        chcolor = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    COLOR += 1
                    if COLOR >= len(COLORS):
                        COLOR = 0
        
        left, middle, right = pg.mouse.get_pressed()
        if left:
            chcolor = True
        x, y = pg.mouse.get_pos()

        if chcolor:
            i, j = int(x // texscale), int(y // texscale)
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
        for i in range(len(texture)):
            for j in range(len(texture[0])):
                    pg.draw.rect(screen, COLORS[texture[j][i]], [[texscale * i + 1, texscale * j + 1], [texscale - 2, texscale - 2]])
        pg.draw.circle(screen, "GREY", [x, y], 7)
        pg.draw.circle(screen, COLORS[COLOR], [x, y], 6)
        pg.display.update()
    print("[")
    for row in texture[:-1]:
        print(f"    {row},")
    print(f"    {texture[-1]}")
    print("]")
    pg.quit()