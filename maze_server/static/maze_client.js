const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const statusDiv = document.getElementById('status');

let currentMaze = null;
let solutionPath = null;
let dfsPath = null;

function resizeCanvas() {
    const maxWidth = window.innerWidth - 20; // Use almost all horizontal space
    const maxHeight = window.innerHeight * 0.8; // Use more vertical space too
    
    if (currentMaze) {
        // Calculate aspect ratio based on maze dimensions
        const rows = currentMaze.length;
        const cols = currentMaze[0].length;
        const mazeAspectRatio = cols / rows;
        
        // Calculate optimal size while maintaining aspect ratio
        let canvasWidth = maxWidth;
        let canvasHeight = maxWidth / mazeAspectRatio;
        
        // If height exceeds max, scale down based on height
        if (canvasHeight > maxHeight) {
            canvasHeight = maxHeight;
            canvasWidth = maxHeight * mazeAspectRatio;
        }
        
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;
        
        drawMaze(currentMaze);
    } else {
        // Default size when no maze is loaded
        canvas.width = Math.min(maxWidth, 800);
        canvas.height = Math.min(maxHeight, 600);
    }
}

function setStatus(message, type = '') {
    statusDiv.textContent = message;
    statusDiv.className = `status ${type}`;
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    setStatus('');
}

async function loadMaze() {
    try {
        setStatus('Loading maze...', 'loading');
        
        const response = await fetch('http://127.0.0.1:5000/api/maze');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const mazeData = await response.json();
        
        if (mazeData.map) {
            currentMaze = mazeData.map;
            solutionPath = null;
            dfsPath = null;
            resizeCanvas(); // Resize canvas to fit maze aspect ratio
            setStatus('Maze loaded successfully!', 'success');
        } else {
            throw new Error('Invalid maze data received');
        }
        
    } catch (error) {
        console.error('Error loading maze:', error);
        setStatus(`Error: ${error.message}`, 'error');
    }
}

async function solveMaze() {
    if (!currentMaze) {
        setStatus('Please load a maze first', 'error');
        return;
    }
    
    try {
        setStatus('Solving maze...', 'loading');
        
        const response = await fetch('http://127.0.0.1:5000/api/solve_maze');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const solutionData = await response.json();
        
        if (solutionData.path) {
            solutionPath = solutionData.path;
            dfsPath = null; // Clear DFS path when showing regular solution
            drawMaze(currentMaze);
            setStatus('Maze solved successfully!', 'success');
        } else {
            throw new Error('No solution found');
        }
        
    } catch (error) {
        console.error('Error solving maze:', error);
        setStatus(`Error: ${error.message}`, 'error');
    }
}

async function solveDFS() {
    if (!currentMaze) {
        setStatus('Please load a maze first', 'error');
        return;
    }
    
    try {
        setStatus('Solving maze with DFS...', 'loading');
        
        const response = await fetch('http://127.0.0.1:5000/api/solve_dfs');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const solutionData = await response.json();
        
        if (solutionData.path) {
            dfsPath = solutionData.path;
            solutionPath = null; // Clear regular solution path when showing DFS
            drawMaze(currentMaze);
            setStatus('Maze solved with DFS successfully!', 'success');
        } else {
            throw new Error('No DFS solution found');
        }
        
    } catch (error) {
        console.error('Error solving maze with DFS:', error);
        setStatus(`Error: ${error.message}`, 'error');
    }
}

function drawMaze(maze) {
    clearCanvas();
    
    if (!maze || maze.length === 0) {
        setStatus('No maze data to display', 'error');
        return;
    }
    
    const rows = maze.length;
    const cols = maze[0].length;
    
    const cellWidth = canvas.width / cols;
    const cellHeight = canvas.height / rows;
    
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const x = col * cellWidth;
            const y = row * cellHeight;
            
            // Check if this cell is part of the solution paths
            const isInSolutionPath = solutionPath && solutionPath.some(point => 
                point[0] === row && point[1] === col
            );
            const isInDFSPath = dfsPath && dfsPath.some(point => 
                point[0] === row && point[1] === col
            );
            
            if (maze[row][col] === '*') {
                ctx.fillStyle = '#800080';
                ctx.fillRect(x, y, cellWidth, cellHeight);
            } 
            else if (maze[row][col] === 'S') {
                ctx.fillStyle = '#f000f0';
                ctx.fillRect(x, y, cellWidth, cellHeight);
            }
            else if (maze[row][col] === 'E') {
                ctx.fillStyle = 'green';
                ctx.fillRect(x, y, cellWidth, cellHeight);
            }
            else if (isInSolutionPath) {
                ctx.fillStyle = '#ffff00'; // Yellow for regular solution
                ctx.fillRect(x, y, cellWidth, cellHeight);
            }
            else if (isInDFSPath) {
                ctx.fillStyle = '#ff6600'; // Orange for DFS path
                ctx.fillRect(x, y, cellWidth, cellHeight);
            }
            else {
                ctx.fillStyle = 'white';
                ctx.fillRect(x, y, cellWidth, cellHeight);
            }
            
            ctx.strokeStyle = '#ddd';
            ctx.lineWidth = 0.5;
            ctx.strokeRect(x, y, cellWidth, cellHeight);
        }
    }
}

// Initialize status message when page loads
document.addEventListener('DOMContentLoaded', function() {
    resizeCanvas();
    setStatus('Click "Load Maze" to fetch and display the maze');
});

// Handle window resize
window.addEventListener('resize', resizeCanvas);