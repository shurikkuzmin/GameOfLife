#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 09:52:10 2022

@author: shurik
"""

import numpy
import pygame

size = 100
field = numpy.zeros((size, size))

pygame.init()

WINDOW = pygame.display.set_mode((500,500))
WINDOW.fill((0,0,0))

isActive = True
while isActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False

pygame.quit()

print(field)