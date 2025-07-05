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

# Function to read a maze from maze.txt file
def generate_maze(filename='maze.txt'):
    """
    Read maze from a text file
    """
    maze = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove newline character and add to maze
                maze.append(line.rstrip('\n'))
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []
    return maze


class Maze(object):
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


    def number_of_new_neighbors(self, x, y, visited):
        """
        Returns the number of unvisited neighbors that are open paths or the exit.
        """
        count = 0
        neighbors = [
            (0, 1), (1, 0),
            (0, -1), (-1, 0)
        ]
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.MAZE_W and 0 <= ny < self.MAZE_H:
                if (nx, ny) not in visited and (self.maze[nx][ny] == ' ' or self.maze[nx][ny] == 'E'):
                    count += 1
        return count
    
    def backtrack_path(self, visited, exit_point, parent):
        """
        Backtrack to find the path from the exit point to the start point.
        
        Args:
            visited: Set of visited coordinates
            exit_point: The coordinates of the exit point
            
        Returns:
            List of coordinates representing the path from start to exit
        """
        path = []
        current = exit_point
        
        while current in visited:
            path.append(current)
            print("Current position:", current)
            # Find the parent of the current node
            current = parent.get(f"{current[0], current[1]}", None)
        return path[::-1]  # Reverse the path to get it from start to exit

    def solve(self):
        """
        Solve the maze using a simple algorithm (e.g., DFS or BFS)
        This is a placeholder for future implementation.
        """
        stack = [(self.myX, self.myY)]
        path = []
        visited = set()
        parent =  {}
        while stack:
            x, y = stack.pop()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # Check if exit is reached
            if self.maze[x][y] == 'E':
                print("Exit found at:", (x, y))
                return self.backtrack_path(visited, (x, y), parent)
            
            # Explore neighbors
            n= [
                (0, 1), (1, 0),
                (0, -1), (-1, 0)
               ]
            
            random.shuffle(n)
            for dx, dy in n:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < self.MAZE_W and 0 <= new_y < self.MAZE_H and \
                   (new_x, new_y) not in visited and \
                   (self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == 'E'):
                    stack.append((new_x, new_y))
                    parent[f"{new_x,new_y}" ] = (x,y)
        return []

    def solve_dfs(self):
        """
        Solve the maze using a simple algorithm (e.g., DFS or BFS)
        This is a placeholder for future implementation.
        """
        stack = [(self.myX, self.myY)]
        path = []
        visited = set()
        parent =  {}
        while stack:
            x, y = stack.pop()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            path.append((x, y))

            # Check if exit is reached
            if self.maze[x][y] == 'E':
                print("Exit found at:", (x, y))
                return path
            
            # Explore neighbors
            n= [
                (0, 1), (1, 0),
                (0, -1), (-1, 0)
               ]
            
            random.shuffle(n)
            for dx, dy in n:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < self.MAZE_W and 0 <= new_y < self.MAZE_H and \
                   (new_x, new_y) not in visited and \
                   (self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == 'E'):
                    stack.append((new_x, new_y))
                    parent[f"{new_x,new_y}" ] = (x,y)
        return []


    def solve_bfs(self):
        queue = deque([(self.myX, self.myY)])
        parent =  {}
        visited = set()
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            # Check if exit is reached
            if self.maze[x][y] == 'E':
                print("Exit found at:", (x, y))
                return self.backtrack_path(visited, (x, y), parent)
            
            # Explore neighbors
            n= [
                (0, 1), (1, 0),
                (0, -1), (-1, 0)
               ]
            
            random.shuffle(n)
            for dx, dy in n:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < self.MAZE_W and 0 <= new_y < self.MAZE_H and \
                   (new_x, new_y) not in visited and \
                   (self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == 'E'):
                    queue.append((new_x, new_y))
                    parent[f"{new_x,new_y}" ] = (x,y)

if __name__ == '__main__':
    maze_map = generate_maze("maze_small.txt")

    # Create a maze instance, set the maze, display it, and start the game
    m = Maze()
    m.setMaze(maze_map)
    m.display()

    #path= m.solve()
    #print("Path found:", path)

    m.game()

    m.display_path(path)                    