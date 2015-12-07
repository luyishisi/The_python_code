#coding:utf-8
import pygame 
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (1280,800)

screen = pygame.display.set_mode(screen_size, 0 ,32)
#初始化屏幕，大小1280*800，不使用特殊，32色。
font = pygame.font.SysFont("arial",16);
font_height = font.get_linesize()
event_text = []
#调用系统字体，获取行高的数值，建立一个列表用来存放事件

while True:

    event = pygame.event.wait()
    event_text.append(str(event))
#建立事件等待，获取到就转换成字符串给列表。
    event_text = event_text[-screen_size[1]/font_height:]
#切片处理，暂时还没有领悟，大概作用是一次只保留屏幕所能显示的那部分
    if event.type == QUIT:
        exit()

    screen.fill((0,0,0))
#设置背景色，0,0,0就是全黑
    y = screen_size[1]-font_height

    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))

        y -= font_height
#这里是打印出所有事件。
    pygame.display.update()

