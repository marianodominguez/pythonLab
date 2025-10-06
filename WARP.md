# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Development Commands

### Running the Maze Visualizer (Main Project)
```bash
# Navigate to the maze server directory
cd maze_server

# Install dependencies
pip install -r requirements.txt

# Set Python path to include the root directory (required for maze imports)
export PYTHONPATH=..:$PYTHONPATH

# Run the Flask development server
python app.py

# Access the web interface at http://localhost:5000
```

### Testing Individual Components
```bash
# Test binary tree algorithms
python testTree.py

# Test graph algorithms  
python testGraph.py

# Test hash table implementation
python testHT.py

# Test maze logic (requires pygame)
cd maze
pip install -r requirements.txt
python testMaze.py
```

### Running Python Challenge Solutions
```bash
# Individual challenge solutions
python pythonChallenge/src/pc01_decode.py
python pythonChallenge/src/pc02_ocr.py
# ... etc for pc01-pc17
```

## Architecture Overview

### Core Structure
This is an educational Python repository with a **modular, separation-of-concerns architecture**:

- **`algorithms/`** - Reusable algorithm implementations (BinaryTree, Graphs, hashtable) that can be imported by other components
- **`maze/`** - UI-agnostic maze logic and algorithms, designed to be consumed by different display systems
- **`maze_server/`** - Web-based visualization layer that consumes the maze logic via imports
- **`pythonChallenge/`** - Standalone programming challenge solutions
- **Root files** - Utility modules and component-specific test files

### Key Architectural Patterns

**Import Dependencies**: The maze_server Flask app imports maze logic via `from maze.Maze import Maze`. The PYTHONPATH must include the repository root for cross-directory imports to work.

**Algorithm Separation**: Core algorithms in `algorithms/` are implemented as standalone classes that can be imported and tested independently.

**Web API Pattern**: The Flask app (`maze_server/app.py`) provides REST endpoints that wrap the core maze logic:
- `GET /api/maze` - Load/generate maze data
- `GET /api/solve_maze` - Return optimal solution path  
- `GET /api/solve_dfs` - Return DFS solution path
- `GET /api/newmaze` - Generate new random maze

**Frontend-Backend Separation**: The JavaScript client (`maze_server/static/maze_client.js`) handles all visualization on HTML5 Canvas, while the Python backend only provides data via JSON APIs.

### Testing Strategy
- **Component Testing**: Individual test files (`testTree.py`, `testGraph.py`, etc.) for each major component
- **Integration Testing**: `maze/testMaze.py` tests the complete maze system including display
- **Manual Testing**: Web interface provides interactive testing of the full maze visualization pipeline

### Data Flow
1. **Maze Logic** (`maze/Maze.py`) - Core maze generation, solving algorithms (BFS, DFS), and game state management
2. **Web API** (`maze_server/app.py`) - Flask endpoints that instantiate Maze objects and return JSON responses  
3. **Client Visualization** (`maze_server/static/maze_client.js`) - Fetches data via API calls and renders on responsive HTML5 Canvas

### Key Dependencies
- **Flask** - Web framework for the API server
- **pygame** - Required for the legacy display components in maze/
- **Standard Library** - Most algorithms use only Python standard library (collections, random, etc.)

### Important Implementation Details
- Maze coordinates use `(x, y)` where x is row and y is column
- The Flask app changes working directory to `../maze` for file operations
- Canvas rendering maintains aspect ratio while being responsive to window size
- Both BFS and DFS solving algorithms are implemented with different return path formats