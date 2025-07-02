'''
Created on Apr 17, 2011

@author: mariano
'''

import pygame
import sys
from pygame.locals import *

class Maze(object):
    '''
    Create and display a maze from strings, with the following format
    S*********\n
     ** ***  *\n
             E\n
    '''

    mode = width,height = 800,600
    maze = []
    myX, myY = (1,2)
    screen = None
    hscale,vscale=(1.0,1.0)
    MAZE_W,MAZE_H = (100,100)
    WALL_COLOR = (100, 30, 100)
    START_COLOR = (0, 255, 0)
    END_COLOR = (255, 0, 0)

    def __init__(self,params=[]):
        '''
        Constructor
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(self.mode)
        self.hscale = (self.width) / self.MAZE_W
        self.vscale = (self.height) / self.MAZE_H
        self.maze = [];
        self.myX, self.myY = (1,1)
        

    def display(self):
        self.screen.fill((0,0,0))
        for x,row in enumerate(self.maze):
            for y,cell in enumerate(row):
                rect = pygame.Rect(x*self.hscale, y*self.vscale, self.hscale, self.vscale)
                if cell== 'S':
                    pygame.draw.rect(self.screen, self.START_COLOR, rect)
                if cell== '*':
                    pygame.draw.rect(self.screen, self.WALL_COLOR, rect)
                if cell == 'E':
                    pygame.draw.rect(self.screen, self.END_COLOR, rect)
            

    def setMaze(self,mazeString = [' S ', '   ', ' E ']):
        for row in mazeString:
            self.maze.append(row)
        self.MAZE_W = len(mazeString[0])
        self.MAZE_H = len(mazeString)
        self.hscale = (self.width) / self.MAZE_W
        self.vscale = (self.height) / self.MAZE_H
        #print self.maze

    def move(self,dir):        
        if dir=='U':
            if self.myY-1 >= 0 and self.maze[self.myX][self.myY-1] == ' ' :
                self.myY -= 1
        if dir=='D':
            if self.myY+1 <= self.MAZE_H and self.maze[self.myX][self.myY+1] == ' ':
                self.myY += 1
        if dir=='L':
            if self.myX-1 >= 0 and self.maze[self.myX-1][self.myY] == ' ' :
                self.myX -= 1
        if dir=='R':
            if self.myX+1 <= self.MAZE_W and self.maze[self.myX+1][self.myY] == ' ':
                self.myX += 1

    def game(self):
        while True:
            rect = pygame.Rect(self.myX*self.hscale,self.myY*self.vscale,self.hscale,self.vscale)
            pygame.draw.rect(self.screen, (0,0,0), rect)
 
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move("U")
                    if event.key == pygame.K_DOWN:
                        self.move("D")
                    if event.key == pygame.K_LEFT:
                        self.move("L")
                    if event.key == pygame.K_RIGHT:
                        self.move("R")
                
                rect = pygame.Rect(self.myX*self.hscale,self.myY*self.vscale,self.hscale,self.vscale)
                pygame.draw.rect(self.screen, (255,255,255), rect)
                pygame.display.update()
                 
