from time import sleep
from DisplayMaze import Maze, generate_maze

# Read maze from file
maze_map = generate_maze()

# Create a maze instance, set the maze, display it, and start the game
m = Maze()
m.setMaze(maze_map)
m.display()

path= m.solve_dfs()
m.display_path(path, 'blue')

m.display()
path= m.solve()
m.display_path(path)
sleep(2)