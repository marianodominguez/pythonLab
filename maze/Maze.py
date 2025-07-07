'''
Created on Apr 17, 2011

@author: mariano
'''

import sys
import random
from time import sleep
from collections import deque


class Maze(object):
    '''
    Create and display a maze from strings, with the following format
    S*********\n
     ** ***  *\n
             E\n
    '''
    maze = []
    myX, myY = (1,2)

    # Function to read a maze from maze.txt file
    def generate_maze(self,filename='maze.txt'):
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

    def setMaze(self,mazeString = ['*S*', '* *', '*E*']):
        for row in mazeString:
            if 'S' in row:
                self.myX = mazeString.index(row)
                self.myY = row.index('S')
            self.maze.append(row)
        self.MAZE_W = len(mazeString)
        self.MAZE_H = len(mazeString[0])
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

                