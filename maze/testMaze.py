from time import sleep
from Maze import Maze
from DisplayMazeApp import MazeApp

# Read maze from file

# Create a maze instance, set the maze, display it, and start the game
m = Maze()
app = MazeApp()
maze_map = m.generate_maze()
m.setMaze(maze_map)
app.setMaze(maze_map)

app.display()
sleep(1)

path= m.solve_dfs()
app.display_path(path, 'white')

app.display()
path= m.solve()
app.display_path(path)
app.wait_for_exit()