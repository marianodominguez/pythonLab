#!/bin/python 

import os, sys
import pygame
import math
import random
from pygame.locals import *


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

sqrt_2 = math.sqrt(2)


def cone():
  for th in xrange(0,360, 2):
    x1=200 * math.sin(math.radians(th))
    y1=200 * math.cos(math.radians(th))
    pygame.draw.aaline(screen, (0,255,255) , adjxy(-250 , -200), adjxy(x1,y1) )

def triangle():
  for x in xrange(-width/2,width/2,5):
    pygame.draw.aaline(screen, (0,0,255) , adjxy(0,0), adjxy(x,height/2) )
    
def diamond():
    r = 300
    for i in xrange(0, 360, 15):
        x=r * math.sin(math.radians(i))
        y=r * math.cos(math.radians(i))
        for j in xrange (0, 360, 15):
            x1=r * math.sin(math.radians(j))
            y1=r * math.cos(math.radians(j))
            pygame.draw.aaline(screen, (128,0,255) , adjxy(x,y), adjxy(x1,y1) )
    
def curve():
    r = 250
    for th in xrange(0,360):
        x = r * math.sin(math.radians(th))
        y = r * math.cos(math.radians(th))
        x1= r * math.cos(math.radians(th)*2)
        y1= r * math.cos(math.radians(th)*2)
        pygame.draw.aaline(screen, (0,255,255) , adjxy(x ,y), adjxy(x1,y1) )

def curve2():
    r = 200
    for th in xrange(0,360):
        x = r * math.sin(math.radians(th))
        y = r * math.cos(math.radians(th))
        x1= (r+60) * math.cos(math.radians(th))
        y1= (r+60) * math.cos(math.radians(th))
        pygame.draw.aaline(screen, (255,255,123) , adjxy(x,y), adjxy(x1,y1) )
        #screen.set_at(adjxy(x,y), (0,255,255))
        #screen.set_at(adjxy(x1,y1), (255,255,0))        
        

def sierpinski_chaos():
    vertex = [(0, height/2), (-width/2, -height/2), (width/2, -height/2)]
    point = (0, height/2)
    for i in xrange(100000):
        randomVertex = vertex[random.randint(0,2)]
        midpoint = (( randomVertex[0] + point[0] )/2, ( randomVertex[1] + point[1] )/2)
        screen.set_at(adjpt(midpoint), (0,255,255))
        point = midpoint

def sierpinski(level, (vx, vy), l):
    if level==0:
        if (l<=1):
            screen.set_at((vx,vy), (0,255,255))            
        p1 = (vx, vy)
        p2 = (vx - l/2, vy + l/2)
        p3 = (vx + l/2, vy + l/2)
        pygame.draw.polygon(screen, (0,255,255), [p1, p2, p3])
    else:
        sierpinski(level-1 , (vx,vy) , l/2)
        sierpinski(level-1 , (vx - l/4 ,vy + l/4) , l/2)
        sierpinski(level-1 , (vx + l/4 ,vy + l/4) , l/2)        

def FD(l):
    global xpos,ypos,alpha
    newx, newy = xpos + l*math.sin(alpha), ypos + l*math.cos(alpha)
    pygame.draw.aaline(screen, (0,255,255), (xpos , ypos),(newx, newy))
    xpos,ypos = newx,newy

def dragon(level, l, i):
    global alpha
    if level==0:
        FD(l)
        alpha += math.radians(90 * i)
        FD(l)
    else:
        alpha -= math.radians(45)
        dragon(level - 1, side(l), 1)
        alpha += math.radians(90 * i)        
        dragon(level - 1, side(l), -1)
        alpha += math.radians(45)
             
def adjxy(x,y):
    return (x + width/2, height/2 -y)

def adjpt(point):
    return adjxy(point[0], point[1])

def side(x):
    return x/2 * sqrt_2 

mode = width,height = 1000,800

pygame.init()
screen = pygame.display.set_mode(mode)
l = 0    
ld =0

while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
        sys.exit()
    elif event.type == KEYDOWN:
      screen.fill((0,0,0))
      if event.key == pygame.K_1:
          cone()
      if event.key == pygame.K_2:
          triangle()
      if event.key == pygame.K_3:
          diamond()
      if event.key == pygame.K_4:
          curve()
      if event.key == pygame.K_5:
          sierpinski(l, (width /2, 0 ), 800)
          if l<8: l = l+1
          else : l=0
      if event.key == pygame.K_6:
          alpha=0
          xpos, ypos = width/2,120          
          dragon(ld, 300, 1)
          if ld<18: ld +=1
          else : ld=0
      if event.key == pygame.K_7:
          curve2()
      if event.key == pygame.K_8:
          sierpinski_chaos()
  pygame.display.update()
  
