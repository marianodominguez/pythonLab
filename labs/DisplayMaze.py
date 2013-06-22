'''
Created on Apr 17, 2011

@author: mariano
'''

import pygame
import sys
from pygame.locals import *

MAZE_W,MAZE_H = (100,100)
WALL_COLOR = (100, 30, 100)
START_COLOR = (0, 255, 0)
END_COLOR = (255, 0, 0)

mode = width,height = 800,600
maze = []
myX, myY = (1,2)
screen = None
hscale,vscale=(1.0,1.0)

class Maze(object):
    '''
    Create and display a maze from strings, with the following format
    S*********\n
     ** ***  *\n
             E\n
    '''

    def __init__(self,params=[]):
        '''
        Constructor
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(mode)
        self.hscale = (width) / MAZE_W
        self.vscale = (height) / MAZE_H
        self.maze = [];
        self.myX, self.myY = (1,1)
        

    def display(self):
        self.screen.fill((0,0,0))
        for y,row in enumerate(self.maze):
            for x,cell in enumerate(row):
                rect = pygame.Rect(x*self.hscale, y*self.vscale, self.hscale, self.vscale)
                if cell== 'S':
                    pygame.draw.rect(self.screen, START_COLOR, rect)
                if cell== '*':
                    pygame.draw.rect(self.screen, WALL_COLOR, rect)
                if cell == 'E':
                    pygame.draw.rect(self.screen, END_COLOR, rect)
            

    def setMaze(self, mazeString = [' S ', '   ', ' E ']):
        for row in mazeString:
            self.maze.append(row)
        self.MAZE_W = len(mazeString[0])
        self.MAZE_H = len(mazeString)
        self.hscale = (width) / self.MAZE_W
        self.vscale = (height) / self.MAZE_H

    def game(self):
        while True:
            rect = pygame.Rect(self.myX*self.hscale, self.myY*self.vscale, self.hscale, self.vscale)
            pygame.draw.rect(self.screen, (0,0,0), rect)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:    
                    if event.key == pygame.K_UP:
                        if self.myY > 0: self.myY -= 1
                    if event.key == pygame.K_DOWN:
                        if self.myY < MAZE_H : self.myY += 1
                    if event.key == pygame.K_LEFT:
                        if self.myX > 0: self.myX -= 1
                    if event.key == pygame.K_RIGHT:
                        if self.myX < MAZE_W: self.myX += 1
                rect = pygame.Rect(self.myX*self.hscale, self.myY*self.vscale, self.hscale, self.vscale)
                pygame.draw.rect(self.screen, (255,255,255), rect)
                pygame.display.update()
                 