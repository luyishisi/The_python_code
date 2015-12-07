#coding:utf-8
import pygame
from pygame.locals import *
from sys import exit

background_image_filename = '1.1.jpg'

pygame.init()
screen = pygame.display.set_mode((1280,800),0,32)
background = pygame.image.load(background_image_filename).convert()
#以上的请看前几篇的解释。
x,y=0,0
move_x ,move_y = 0,0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
        #开始检测，是否按键下面的很直观就是表现移动值
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x ,move_y = 0,0
#这里很精妙了，因为把原文中的缩进提前，下面的五行都属于while中了，所以自然会一直的被捕捉到。
    x += move_x
    y += move_y

    screen.fill((0,0,0))
    screen.blit(background,(x,y))
    pygame.display.update()
