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

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW = pygame.display.set_mode((500,500))
WINDOW.fill(BLACK)

def draw_field(field):
    for i in range(size):
        for j in range(size):
            if field[i][j] == 1:
                pygame.draw.rect(WINDOW, WHITE, (5*j, 5*i, 5, 5))


isActive = True
while isActive:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
    draw_field(field)
    pygame.display.update()

pygame.quit()

print(field)