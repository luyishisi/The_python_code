import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((1024,800),0,32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    rand_col = (randint(0,255),randint(0,255),randint(0,255))
    for _ in xrange(100):
        rand_pos = (randint(0,1024),randint(0,799))
        screen.set_at(rand_pos,rand_col)

    pygame.display.update()


	



