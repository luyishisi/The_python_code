# -*- coding: utf-8 -*-
# 记住上面这行是必须的，而且保存文件的编码要一致！
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((1280, 800), 0, 32)
 
#font = pygame.font.SysFont("仿宋_GB2312", 40)
#上句在Linux可行，在我的Windows 7 64bit上不行，XP不知道行不行
#font = pygame.font.SysFont("simsunnsimsun", 40)
#用get_fonts()查看后看到了这个字体名，在我的机器上可以正常显示了
font = pygame.font.Font("仿宋_GB2312.ttf", 40)
#这句话总是可以的，所以还是TTF文件保险啊
text_surface = font.render(u"你好", True, (0, 0, 255))
 
x = 0
y = (800 - text_surface.get_height())/2
 
background = pygame.image.load("1.1.jpg").convert()
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.blit(background, (0, 0))
 
    x -= 2  # 文字滚动太快的话，改改这个数字
    if x : 
        x -= text_surface.get_width()
    else:
        x = 1280 - text_surface.get_width()
 
    screen.blit(text_surface, (x, y))
 
    pygame.display.update()
