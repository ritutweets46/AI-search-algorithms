### Project Overview
This repository contains a comprehensive implementation of search algorithms for solving a matrix search problem. The goal is to find a target element e in an NxN matrix using various search strategies.

### Problem Description
#### Input

- N: Size of the NxN matrix (5, 6, or 7 based on roll number modulus 3)
- e: Target element to search within the matrix

#### Output

- Path taken to reach the target element from the start state
- Current state at each step (Each state is represented by its row and column index)

#### Matrix Generation

- Random integers between 1 and 1000
- Target element e randomly placed
- Start state: Last column of the first row (The start state is always the last column of the first row ((0, N-1)))

The implemented search algorithms are:

1. Depth-First Search (DFS) : explores the search space deeply before backtracking
2. Breadth-First Search (BFS) : explores all nodes level by level
3. Uniform Cost Search (UCS) : finds the shortest cost path to the target
4. Greedy Search : uses a heuristic to guide the search to the target
5. A* Search : combines UCS and Greedy by using both path cost and a heuristic


#### Folder Structure
|-- README.md
|-- DFS_Search.py          # Depth-First Search implementation
|-- BFS_Search.py          # Breadth-First Search implementation
|-- UCS_Search.py          # Uniform Cost Search implementation
|-- Greedy_Search.py       # Greedy Search implementation
|-- A_Star_Search.py        # A* Search implementation


#### Requirements
- Python >= 3.8
- Required libraries:
    - random (for matrix generation)
    - heapq (for priority queue implementation)

### Observations:

1. A* consistently finds the optimal path efficiently due to its balanced heuristic and cost evaluation.
2. Greedy is fast but may take suboptimal paths.
3. BFS guarantees the shortest path in terms of steps but can be memory-intensive.
4. DFS can get stuck in deep branches, requiring more backtracking.