#coding:utf-8
'''
本测试样例将创建一个窗口，然后显示一张图片，
'''
#!/usr/bin/env python

background_image_filename = '1.jpg'
mouse_image_filename = '2.jpg'
#制定图像文件名称

import pygame
from pygame.locals import *
from sys import exit
#从sys中使用结束函数

pygame.init()
#初始化pygame、

screen = pygame.display.set_mode((640,480),0,32)
#创建一个窗口,并且制定大小。

pygame.display.set_caption("hello, world! ly first game!")
#设置窗口标题

background = pygame.image.load(background_image_filename).convert()

mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
           #若接受到退出事件后退出程序 
    screen.blit(background,(0,0))
    #画出背景图
    x,y = pygame.mouse.get_pos()
    #获取鼠标的坐标
    x -= mouse_cursor.get_width()/2
   #获取鼠标图像的宽高计算新的xy的值，目的是为了能居中
    y -= mouse_cursor.get_height()/2
    
    screen.blit(mouse_cursor,(x,y))
    #在新的值画上x，y。以及鼠标的图案。
    pygame.display.update()
    #刷新一下画面
