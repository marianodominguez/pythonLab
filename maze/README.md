# Maze Module

This folder contains all logic and utilities for maze generation, solving, and testing. All code here is UI-agnostic unless otherwise noted, making it reusable for different interfaces (web, CLI, etc.).

## Contents

- **Maze.py**  
  Core maze logic. Provides the `Maze` class for:
  - Generating random mazes
  - Setting and retrieving maze state
  - Solving mazes using different algorithms (BFS, DFS, etc.)

- **algorithms.py** *(optional)*  
  Additional or experimental maze algorithms and utilities. Can be imported by `Maze.py` for advanced features.

- **testMaze.py**  
  Example and test script for the maze logic.  
  - Generates a maze, solves it with both DFS and the standard algorithm, and displays the results.
  - Uses `MazeApp` from `DisplayMazeApp.py` for simple command-line visualization.

- **DisplayMazeApp.py**  
  (optional) non-web visualization app for mazes.  
  - Not required for core logic or web interface.

- **Maze data files**  
  Example mazes in `.txt` format for testing and experimentation.

## Example Usage

```python
from Maze import Maze

m = Maze()
maze_map = m.generate_maze()
m.setMaze(maze_map)
solution = m.solve()      # Standard algorithm
dfs_solution = m.solve_dfs()  # DFS algorithm