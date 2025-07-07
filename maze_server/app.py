from flask import Flask, jsonify, render_template
from maze.Maze import Maze
import os

app = Flask(__name__)
m = Maze()
maze_map = None

@app.route('/api/maze', methods=['GET'])
def handle():
    global maze_map,m
    if maze_map is None:
        # Generate a new maze if it hasn't been generated yet
        os.chdir("../maze")
        maze_map = m.generate_maze()
        m.setMaze(maze_map)
    return jsonify({'map': maze_map})

@app.route('/api/solve_maze', methods=['GET'])
def solve():
    global maze_map,m
    if maze_map is None:
        os.chdir("../maze")
        maze_map = m.generate_maze()
    m.setMaze(maze_map)
    path= m.solve()
    return jsonify({'path': path})

@app.route('/api/solve_dfs', methods=['GET'])
def solve_dfs():
    global maze_map,m
    if maze_map is None:
        os.chdir("../maze")
        maze_map = m.generate_maze()
    m.setMaze(maze_map)
    path= m.solve_dfs()
    return jsonify({'path': path})

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/maze_client.js')
def maze_client_js():
    return app.send_static_file('maze_client.js')

if __name__ == '__main__':
    app.run(debug=True)