#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:52:10 2022

@author: shurik
"""

import numpy
import pygame

size = 100
field = numpy.zeros((size, size))  #numpy.random.randint(0, 2, (size, size))

# Hive
# field[49][50] = 1
# field[50][49] = 1
# field[50][51] = 1
# field[51][49] = 1
# field[51][51] = 1
# field[52][50] = 1

# # Boat
# field[19][19] = 1
# field[20][18] = 1
# field[20][20] = 1
# field[21][19] = 1
# field[21][21] = 1
# field[22][20] = 1
# field[22][22] = 1
# field[23][21] = 1
# field[23][22] = 1

# # Glider
# field[60][60] = 1
# field[61][61] = 1
# field[62][59] = 1
# field[62][60] = 1
# field[62][61] = 1

# Glider gun
#41
#........................O........... 40
#......................O.O........... 41
#............OO......OO............OO 42
#...........O...O....OO............OO 43
#OO........O.....O...OO.............. 44
#OO........O...O.OO....O.O........... 45
#..........O.....O.......O........... 46
#...........O...O.................... 47
#............OO...................... 48
field[40][65] = 1
field[41][63] = 1
field[41][65] = 1
field[42][61] = 1
field[42][62] = 1
field[42][54] = 1
field[42][53] = 1
field[42][75] = 1
field[42][76] = 1
field[43][52] = 1
field[43][56] = 1
field[43][61] = 1
field[43][62] = 1
field[43][75] = 1
field[43][76] = 1
field[44][41] = 1
field[44][42] = 1
field[44][51] = 1
field[44][57] = 1
field[44][61] = 1
field[44][62] = 1

field[45][41] = 1
field[45][42] = 1
field[45][51] = 1
field[45][55] = 1
field[45][57] = 1
field[45][58] = 1
field[45][63] = 1
field[45][65] = 1

field[46][51] = 1
field[46][57] = 1
field[46][65] = 1

field[47][52] = 1
field[47][56] = 1
field[48][53] = 1
field[48][54] = 1



quad_size = 5

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WINDOW = pygame.display.set_mode((size*quad_size, size*quad_size))
WINDOW.fill(BLACK)

def draw_field(field):
    for i in range(size):
        for j in range(size):
            if field[i][j] == 1:
                pygame.draw.rect(WINDOW, WHITE, (quad_size*j, quad_size*i, quad_size, quad_size))

def update_field(field):
    field2 = numpy.zeros_like(field)
    for i in range(size):
        for j in range(size):
            sum_neighbors = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if k==0 and l==0:
                        continue
                    if i+k < 0:
                        continue
                    if i+k > size-1:
                        continue
                    if j+l < 0:
                        continue
                    if j+l > size-1:
                        continue
                    if field[i+k][j+l] == 1:
                        sum_neighbors = sum_neighbors + 1
            if field[i][j] == 1:
                if sum_neighbors == 2 or sum_neighbors == 3:
                    field2[i][j] = 1
            else:
                if sum_neighbors == 3:
                    field2[i][j] = 1
    print("Iteration happened!")
    return field2

isActive = True
while isActive:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
    field = update_field(field)
    draw_field(field)
    pygame.display.update()

pygame.quit()

print(field)