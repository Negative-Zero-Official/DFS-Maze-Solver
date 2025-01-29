# Maze Solver

This Python program finds a path from a start node to a finish node in a maze, represented by a graph, using the Depth-First Search (DFS) algorithm.

## How to Use

1. Represent the graph in an Adjacency List (hard-coded in this project, you can edit the code to represent your maze.)
2. Save the `MazeSolver.py` file.
3. Run the program!  
It's that simple.

## Code Explanation

### find_exit(graph, start, finish)

This is the function that defines and performs a DFS to find a path from the start node to the finish node.

- **Parameters**
    - graph: A dictionary representing the maze
    - start: The starting node identifier.
    - finish: The finishing node identifier.

- **Inner Function**
    - `DFS(node)`: The actual DFS function; A recursive function that explores the graph. It adds each node visited to the path list, and pops them out of the list if it backtracks from the node. The resulting path list is the path from the start to the exit.

### main()

The main function. Here, the graph is initialized and defined and simply calls the find_exit() method.

## Maze visualization
This is the visualization of the example maze that is hard-coded into this program.  
![Maze Visualization](https://github.com/Negative-Zero-Official/DFS-Maze-Solver/blob/main/MazeExample.png)

## Output
```
Found path to exit: 2 -> 1 -> 6 -> 11 -> 12 -> 17 -> 18 -> 19 -> 14 -> 9 -> 10 -> 5
```
