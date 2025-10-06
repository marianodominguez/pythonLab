# Python Lab

A collection of Python projects and experiments covering various algorithms, data structures, and applications.

## Featured Project: Maze Visualizer

A web-based maze visualization client that fetches maze data from a Flask API and displays it on an HTML5 canvas with interactive solving capabilities.

### Running the Maze Visualizer

 1. Navigate to the `maze_server` directory
 2. Install dependencies: `pip install -r requirements.txt`
 3. Set path to the root folder:  
    `export PYTHONPATH=..:$PYTHONPATH`
 4. Run the Flask server:  
    `python app.py`
 5. Open browser to `http://localhost:5000`

### Features

- **Responsive Design**: Canvas automatically resizes to fit the browser window while maintaining aspect ratio
- **Multiple Solving Algorithms**: Supports both regular maze solving and Depth-First Search (DFS)
- **Visual Path Highlighting**: Different colors for different solution paths
- **Real-time Status Updates**: Loading states and error handling
- **Clean Interface**: Modern UI with intuitive controls

### Usage

1. **Load Maze**: Click "Load Maze" to fetch maze data from the server
2. **Solve Maze**: Click "Solve Maze" to display the optimal solution path
3. **Solve DFS**: Click "Solve DFS" to display the DFS solution path
4. **Clear Canvas**: Click "Clear Canvas" to reset the display

### Visual Elements

#### Maze Components

- **Purple rectangles** (`#800080`) - Walls (`*`)
- **Magenta squares** (`#f000f0`) - Start position (`S`)
- **Green squares** (`green`) - End position (`E`)
- **White squares** - Empty walkable spaces

#### Solution Paths

- **Yellow path** (`#ffff00`) - Regular solution algorithm
- **Orange path** (`#ff6600`) - DFS solution algorithm

*Note: Only one solution path is displayed at a time*

### Technical Details

#### Canvas Sizing

- **Responsive**: Uses almost full window width (window width - 20px margin)
- **Aspect Ratio**: Maintains maze proportions with square cells
- **Vertical Space**: Uses up to 80% of viewport height
- **Auto-resize**: Automatically adjusts when window is resized

#### API Endpoints

- `GET /api/maze` - Retrieves the current maze data
- `GET /api/solve_maze` - Returns the solution path using standard algorithm
- `GET /api/solve_dfs` - Returns the solution path using Depth-First Search

## Project Structure

### 📁 algorithms/
Core algorithm implementations including:

- **BinaryTree.py** - Binary tree data structure and operations
- **Graphs.py** - Graph algorithms and representations
- **hashtable.py** - Hash table implementation
- **__init__.py** - Package initialization

### 📁 lab/
Experimental projects and exercises:

- **combinations.py** - Combinatorial algorithms
- **opengl/** - OpenGL graphics experiments (gears, 3D shapes, solar system)
- **quiz/** - Quiz applications (caterpillar data processing)
- **twitter/** - Social media analysis tools and bot implementations

### 📁 maze/

Maze generation and solving logic, fully separated from display/UI code:

- **Maze.py** - Core maze logic: generation, solving (BFS, DFS), and data representation. Provides the `Maze` class with methods for creating, solving, and managing maze state.
- **algorithms.py** *(optional)* - Additional maze algorithms or utilities that can be imported by `Maze.py` for advanced maze generation or solving strategies.
- **testMaze.py** - Unit tests and validation for maze logic.
- **DisplayMaze.py** - (Legacy/optional) Visualization utilities for command-line or non-web display.
- Various maze data files (txt format) - Example mazes for testing and experimentation.

> **Note:** All logic in `maze/` is UI-agnostic and can be reused or tested independently of any display code.

### 📁 maze_server/

**Web-based maze visualizer** (Flask server + JavaScript client):

- **app.py** - Flask API server, serving maze data and solutions via REST endpoints.
- **templates/index.html** - Web interface for user interaction.
- **static/maze_client.js** - Interactive canvas client using modern JavaScript (ES6+).
- **requirements.txt** - Python dependencies for the server.

### 📁 pythonChallenge/
Solutions to Python programming challenges:

- **src/** - Challenge solutions (PC01-PC17)
- Image processing, data decoding, and puzzle solving
- OCR, pickle manipulation, and advanced Python techniques

### 📁 Root Files

- **arrays.py** - Array manipulation utilities
- **characters.py** - Character processing functions
- **testGraph.py** - Graph algorithm testing
- **testHT.py** - Hash table testing
- **testTree.py** - Binary tree testing

## Getting Started

### Prerequisites

- Python 3.7+
- Flask (for maze_server)
- Modern web browser with HTML5 Canvas support

### Browser Compatibility

- Requires modern browser with HTML5 Canvas support
- Uses ES6+ features (async/await, arrow functions)
- Responsive design works on desktop and mobile

## Development

### Architecture

- **Modular Design**: Clear separation between maze logic (`maze/`), server API (`maze_server/app.py`), and client visualization (`maze_server/static/maze_client.js`)
- **Async Operations**: Non-blocking API calls with proper error handling
- **Responsive UI**: Canvas adapts to any screen size while maintaining maze proportions
- **Clean Code**: Well-documented functions with clear separation of responsibilities

### Key Technologies

- **Backend**: Python Flask for API server
- **Frontend**: Vanilla JavaScript with HTML5 Canvas
- **Algorithms**: Multiple maze solving implementations
- **UI/UX**: Responsive CSS with modern design patterns

## Contributing

Feel free to explore, modify, and extend any of the projects. Each directory contains focused implementations that can serve as learning resources or starting points for more complex applications.

## License

This project is for educational and experimental purposes.