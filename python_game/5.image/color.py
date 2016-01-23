#coding:utf-8
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)
#画个窗口
color1 = (221,99,20)
color2 = (96,130,51)

factor = 0
def blend_color(color1,color2,blend_factor):
    r1,g1,b1 = color1
    r2,g2,b2 = color2
    r = r1 +(r2 -r1)* blend_factor
    g = g1 +(g2 -g1)* blend_factor
    b = b1 +(b2 -b1)* blend_factor
    return int(r),int(g),int(b)
#此函数是为了每次计算新的颜色数据   
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))
#屏幕的底色
    tri = [(0,120),(639,100),(639,140)]
#
    pygame.draw.polygon(screen,(0,255,0),tri)
    #画出那个绿色的锥心
    pygame.draw.circle(screen,(0,0,0),(int(factor*639.0),120),10)
#画出那个黑球
    x,y = pygame.mouse.get_pos()
    #获取鼠标位置
    if pygame.mouse.get_pressed()[0]:
        factor = x/639.0
        pygame.display.set_caption("pygame color blend test - %.3f" % factor)
    #获取当前鼠标把球移动到的坐标，然后修改窗口标题
    color = blend_color(color1 ,color2,factor)
    #修改颜色
    pygame.draw.rect(screen,color,(0,240,640,240))
    #画出这个区域，1
    pygame.display.update()
