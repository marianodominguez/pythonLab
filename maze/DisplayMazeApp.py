'''
Created on Apr 17, 2011

@author: mariano
'''

import pygame
import sys
import random
from pygame.locals import *
from time import sleep
from collections import deque
from Maze import Maze


class MazeApp(object):
    '''
    Create and display a maze from strings, with the following format
    S*********\n
     ** ***  *\n
             E\n
    '''

    mode = width,height = 1600,1200
    maze = []
    myX, myY = (1,2)
    screen = None
    hscale,vscale=(1.0,1.0)
    MAZE_W,MAZE_H = (100,100)
    WALL_COLOR = (100, 30, 100)
    START_COLOR = (0, 255, 0)
    END_COLOR = (255, 0, 0)

    def init_graph(self,params=[]):
        if not self.screen :
            pygame.init()
            self.screen = pygame.display.set_mode(self.mode)
            self.hscale = (self.width) / self.MAZE_W
            self.vscale = (self.height) / self.MAZE_H
            self.myX, self.myY = (1,1)
        

    def display(self):
        self.init_graph(self)
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
        pygame.display.update()

    def setMaze(self,mazeString = ['*S*', '* *', '*E*']):
        for row in mazeString:
            if 'S' in row:
                self.myX = mazeString.index(row)
                self.myY = row.index('S')
            self.maze.append(row)
        self.MAZE_W = len(mazeString)
        self.MAZE_H = len(mazeString[0])
        self.hscale = (self.width) / self.MAZE_W
        self.vscale = (self.height) / self.MAZE_H
        #print self.maze

    def is_valid_move(self, dx, dy):
        """
        Check if a move is valid (within bounds and target cell is a space or exit)
        
        Args:
            dx: Change in x-coordinate
            dy: Change in y-coordinate
            
        Returns:
            bool: True if the move is valid, False otherwise
        """
        new_x = self.myX + dx
        new_y = self.myY + dy
        
        # Check if the new position is within bounds
        if new_x < 0 or new_x >= self.MAZE_W or new_y < 0 or new_y >= self.MAZE_H:
            return False
            
        # Check if the new position is a space or exit
        return self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == 'E'
    
    def perform_move(self, dx, dy):
        """
        Perform a move in the specified direction
        
        Args:
            dx: Change in x-coordinate
            dy: Change in y-coordinate
            
        Returns:
            bool: True if the exit is reached, False otherwise
        """
        self.myX += dx
        self.myY += dy
        
        # Check if the exit is reached
        return self.maze[self.myX][self.myY] == 'E'
    
    def move(self, dir):
        """
        Move the player in the specified direction
        
        Args:
            dir: Direction to move ('U', 'D', 'L', 'R')
            
        Returns:
            bool: True if the exit is reached, False otherwise
        """
        # Define direction vectors (dx, dy) for each direction
        directions = {
            'U': (0, -1),
            'D': (0, 1),
            'L': (-1, 0),
            'R': (1, 0)
        }
        
        # Get the direction vector
        if dir not in directions:
            return False
            
        dx, dy = directions[dir]
        
        # Check if the move is valid
        if self.is_valid_move(dx, dy):
            # Perform the move and return if exit is reached
            return self.perform_move(dx, dy)
            
        return False

    def game(self):
        font = pygame.font.Font(None, 36)
        exit_reached = False
        
        while True:
            rect = pygame.Rect(self.myX*self.hscale,self.myY*self.vscale,self.hscale,self.vscale)
            pygame.draw.rect(self.screen, (0,0,0), rect)
 
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        exit_reached = self.move("U")
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        exit_reached = self.move("D")
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        exit_reached = self.move("L")
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        exit_reached = self.move("R")
                    # Add WASD as alternative movement keys
                    
                    # Check if exit was reached
                    if exit_reached:
                        text = font.render("Congratulations! Exit reached!", True, (255, 255, 0))
                        text_rect = text.get_rect(center=(self.width/2, self.height/2))
                        self.screen.blit(text, text_rect)
                
                rect = pygame.Rect(self.myX*self.hscale,self.myY*self.vscale,self.hscale,self.vscale)
                pygame.draw.rect(self.screen, (255,255,255), rect)
                pygame.display.update()

    def display_path(self, path, color='cyan'):
        """
        Display the path on the maze
        Args:
        """
        for x, y in path:
            rect = pygame.Rect(x * self.hscale+self.hscale/4, y * self.vscale+self.vscale/4, self.hscale/2, self.vscale/2)
            pygame.draw.rect(self.screen, Color(color), rect)
            pygame.display.update()
    

    def wait_for_exit(self):
        """
        Wait for the user to close the window
        """
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
            sleep(0.1)

if __name__ == '__main__':
    m = Maze()
    app = MazeApp()
    maze_map = m.generate_maze("maze_small.txt")
    app.setMaze(maze_map)
    app.display()
    app.game()
                  