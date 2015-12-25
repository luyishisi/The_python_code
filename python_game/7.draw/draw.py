#!/usr/bin/env python
#coding:utf-8
import pygame
from pygame.locals import *
from sys import exit 
from random import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((1024,800),0,32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            points =[]
            screen.fill((255,255,255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            
            rc = (randint(0,255),randint(0,255),randint(0,255))
            rp = (randint(0,1023),randint(0,799))
            rs = (639-randint(rp[0],1023),799-randint(rp[1],799))
            pygame.draw.rect(screen,rc,Rect(rp,rs))

            rc = (randint(0,255),randint(0,255),randint(0,255))
            rp = (randint(0,1023),randint(0,799))
            rr = randint(1,200)
            pygame.draw.circle(screen,rc,rp,rr)


            x,y = pygame.mouse.get_pos()
            points.append((x,y))

            angle = (x/639.)*pi*2.
            pygame.draw.arc(screen,(0,0,0),(0,0,1024,799),0,angle,3)

            pygame.draw.ellipse(screen,(0,255,0),(0,0,x,y))

            pygame.draw.line(screen,(0,0,255),(0,0),(x,y))
            pygame.draw.line(screen,(255,0,0),(1024,800),(x,y))
            
            if len(points)>1:
                pygame.draw.lines(screen(155,155,0),False,points,2)

            for p in points:
                pygame.draw.circle(screen,(155,155,155),p,3)
    pygame.display.update()


