#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:52:10 2022

@author: shurik
"""

import numpy
import pygame

size = 100
field = numpy.random.randint(0, 2, (size, size))
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