# Maze Visualizer

A web-based maze visualization client that fetches maze data from a Flask API and displays it on an HTML5 canvas with interactive solving capabilities.

## Features

- **Responsive Design**: Canvas automatically resizes to fit the browser window while maintaining aspect ratio
- **Multiple Solving Algorithms**: Supports both regular maze solving and Depth-First Search (DFS)
- **Visual Path Highlighting**: Different colors for different solution paths
- **Real-time Status Updates**: Loading states and error handling
- **Clean Interface**: Modern UI with intuitive controls

## File Structure

```
maze_server/
├── maze/
│   ├── Maze.py           # Core maze logic: generation, solving, and data representation
│   ├── algorithms.py     # (Example) Additional maze algorithms and utilities
│   └── ...               # Other logic modules (no display/UI code)
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   └── maze_client.js    # JavaScript client for visualization and interaction
└── README.md             # This file
```

## Maze Logic (`maze/` directory)

All maze generation and solving logic is now separated into the `maze/` directory. This ensures a clear separation between backend logic and frontend display.

- **Maze.py**  
  Contains the `Maze` class, which provides:
  - Maze generation (e.g., random, recursive backtracking)
  - Maze solving (e.g., shortest path, DFS)
  - Maze data representation (as a 2D list or similar)
  - Methods for setting and retrieving maze state

- **algorithms.py** (if present)  
  Additional algorithms or utilities for maze manipulation, which can be imported and used by `Maze.py`.

- **No UI or Display Code**  
  All code in `maze/` is focused on logic and data, making it reusable and easy to test.

## API Endpoints

The Flask app exposes the following endpoints for the client:

- `GET /api/maze` - Retrieves the current maze data
- `GET /api/solve_maze` - Returns the solution path using the standard algorithm
- `GET /api/solve_dfs` - Returns the solution path using Depth-First Search

## Usage

1. **Load Maze**: Click "Load Maze" to fetch maze data from the server
2. **Solve Maze**: Click "Solve Maze" to display the optimal solution path
3. **Solve DFS**: Click "Solve DFS" to display the DFS solution path
4. **Clear Canvas**: Click "Clear Canvas" to reset the display

## Visual Elements

### Maze Components
- **Purple rectangles** (`#800080`) - Walls (`*`)
- **Magenta squares** (`#f000f0`) - Start position (`S`)
- **Green squares** (`green`) - End position (`E`)
- **White squares** - Empty walkable spaces

### Solution Paths
- **Yellow path** (`#ffff00`) - Regular solution algorithm
- **Orange path** (`#ff6600`) - DFS solution algorithm

*Note: Only one solution path is displayed at a time*

## Technical Details

### Canvas Sizing
- **Responsive**: Uses almost full window width (window width - 20px margin)
- **Aspect Ratio**: Maintains maze proportions with square cells
- **Vertical Space**: Uses up to 80% of viewport height
- **Auto-resize**: Automatically adjusts when window is resized

### Data Format
The client expects maze data in the following JSON format:
```json
{
  "map": [
    ["*", "*", "*", "S", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", "*", " ", "*"],
    ["*", " ", " ", " ", "E"],
    ["*", "*", "*", "*", "*"]
  ]
}
```

Solution paths are returned as arrays of coordinates:
```json
{
  "path": [[0, 3], [1, 3], [2, 3], [3, 3]]
}
```

### Browser Compatibility
- Requires modern browser with HTML5 Canvas support
- Uses ES6+ features (async/await, arrow functions)
- Responsive design works on desktop and mobile

## Development

### HTML Structure
- Clean semantic HTML5 structure
- Responsive CSS with flexible layout
- Bootstrap-like button styling
- Status indicator with color-coded messages

### JavaScript Architecture
- Modular function design
- Async/await for API calls
- Event-driven canvas updates
- Proper error handling and user feedback

### Key Functions
- `loadMaze()` - Fetches and displays maze data
- `solveMaze()` - Solves maze with regular algorithm
- `solveDFS()` - Solves maze with DFS algorithm
- `drawMaze()` - Renders maze and solution paths on canvas
- `resizeCanvas()` - Handles responsive canvas sizing

## CSS Features

- **Responsive Design**: Adapts to different screen sizes
- **Modern Styling**: Clean, professional appearance
- **Interactive Elements**: Hover effects on buttons
- **Status Indicators**: Color-coded feedback (success, error, loading)
- **Minimal Margins**: Maximizes canvas space usage

## Error Handling

The client includes comprehensive error handling:
- Network request failures
- Invalid API responses
- Missing maze data
- Canvas rendering errors
- User feedback for all error states

## Performance Optimizations

- **Efficient Rendering**: Only redraws when necessary
- **Memory Management**: Clears previous paths when loading new solutions
- **Responsive Updates**: Debounced resize events
- **Minimal DOM Manipulation**: Canvas-based rendering for smooth performance

## Future Enhancements

Potential improvements could include:
- Animation of solution path discovery
- Multiple algorithm comparison view
- Maze editing capabilities
- Export functionality for maze images
- Touch/mobile gesture support