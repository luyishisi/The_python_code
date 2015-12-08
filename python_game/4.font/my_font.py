#coding:utf-8
import pygame
from pygame.locals import *

my_name = "你好世界"

pygame.init()
my_font = pygame.font.SysFont("宋体" ,64)
name_surface = my_font.render(my_name,True,(0,0,0),(255,255,255))

pygame.image.save(name_surface,"name.png")


