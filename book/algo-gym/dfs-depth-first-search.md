# Depth-First Search (DFS)

### Q: Is this bottom statement syntactically correct? If not, describe why and how to
fix it.

```python
image: List[List[int]]
max_r: int

max_c = 0 if max_r === 0 else len(image[0])
```

A: It's wrong. The equals operator in Python is "==", not "===" like in TS.

from typing import List, Set, Tuple

def foo(x: List[any]):
    """Docs on foo"""
    return x + 1

foo(1)

x: Set = set([1, 2, 3])


```python
def fill_img(
    image: List[List[int]],
    new_color: int,
    start_pixel: Tuple[int, int],
) -> List[List[int]]:
    """Fills the start pixel and all neighbors of the same color with the new
    color.
    """

    max_row: int = len(image)
    max_c = 0 if max_row == 0 else len(image[0])
    # Columns cannot exist if there aren't rows

    x, y = start_pixel
    assert 0 <= x < max_row and 0 <= y < max_c, (
        f"start pixel {start_pixel} is outside the image or invalid"
    )

    start_color = image[x][y]
    if start_color == new_color:
        return image

    Point = Tuple[int, int]
    visited_pixels: Set[Point] = set()

    def dfs_fill(row: int, col: int):
        """Depth first search N, S, E, W directions inside the image and fill
        them with the new color IFF the pixel has the start color."""
        # Stop conditions
        # Check if row or col are invalid
        # Check if point is visited
        # 
        if (
            (row < 0 or row >= max_row)  # row outside image
            or (col < 0 or col >= max_c)  # col outside image
            or (row, col) in visited_pixels  # row processed already
            or image[row][col] != start_color  # row falls outside criteria for
            # new color. Point must be start_color
        ):
            return

        # rewrite to new color
        image[row][col] = new_color
        visited_pixels.add((row, col))

        # dfs N, S, W, E
        dfs_fill(row - 1, col)
        dfs_fill(row + 1, col)
        dfs_fill(row, col - 1)
        dfs_fill(row, col + 1)

    dfs_fill(x, y)
    return image
```


TODO: Test cases for impl

```python
# Small connected region of 1s
image1 = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

# Fill follows a winding 1-path
image2 = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 1]
]

# 0 is surrounded by 1s; fill from the center
image3 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Diagonals are not connected in 4-directional DFS
image4 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Empty image
image7 = []

# Already filled
image6 = [
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1]
]
```


### Mondai 1: Graph Traversal without Grid

You are given a directed graph represented as an adjacency list. Each key in the graph is a unique node identifier (a string), and the corresponding value is a list of nodes that it directly connects to (its neighbors).

Q: Implement a function that performs a depth-first search (DFS) starting from a given node. Your function should return a list of all nodes reachable from the starting node, in the order they were first visited.

Example: 

Input
```
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
```

Output:
```
['A', 'B', 'D', 'C', 'E', 'F']
```

Constraints:
- All node names are unique strings.
- The graph may contain cycles (but no self-loops).
- You may assume the input graph is valid and all referenced nodes are included.
- You may not revisit nodes 



Q: Why is important to communicate that you "may not revisit nodes"?

This implies we'll need to use a visited set to avoid infinite loops.

Q: Is this problem solvable with both DFS and BFS? If not, why? And if so, when
should you use one versus the other?

Both DFS and BFS are viable. 

BFS is better if you want to know the shortest path
to each reachable node. DFS doesn't guarantee shortest paths.

DFS is better for deep or narrow structures. BFS uses a queue and tends to
consume more memory in wide graphs.


Q: We often say that DFS is implemented with stack and BFS is implemented with a
queue.

How is that the case when using recursion with DFS?

Recursion implements an implicit stack, the call stack. You can also write DFS iteratively with
an explicit stack.

Q: The queue behavior order acronym is "FIFO" (first-in-first-out).

Q: The stack behavior order acronym is "LIFO" (last-in-first-out).

Q: Implement a queue of strings in Python.

```python
from collections import deque

start: str # pretend we have it
queue: deque[str] = deque([start])
```

Q: Queues in Python are imported from what package? 

```
collections.deque
```

Q: What does "deque" mean in Python?

Double-ended queue.

Q: Why use a `deque` instead of a `List` in BFS?

A `deque` (double-ended queue) has O(1) time complexity for popping from teh
left (`deque.popleft`). Whereas, `list.pop(0)` would be O(n) because it shifts
all elements.

Q: In Python, how do you add to a `deque`?

`deque.append`

### Mondai 2: Number of Islands

You are given a 2D grid of '1's (land) and '0's (water). An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Q: Write a function to count the number of distinct islands in the grid.

Example: 

Input
```
grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]
```

Output: 3


### Mondai 3: Path Exists in Maze

You are given a 2D grid representing a maze. Each cell is either open (0) or blocked (1). You are also given a start position and an end position.

Write a function that returns True if there exists a path from the start to the end position using only up, down, left, or right moves without crossing any blocked cells.

Example 
Input
```
maze = [
    [0, 0, 1],
    [1, 0, 1],
    [1, 0, 0]
]
start = (0, 0)
end = (2, 2)
```

Output: 
```
True
```

Constraints:
- `1 <= maze.length`, `maze[0].length <= 100`
- `maze[r][c]` is either 0 (open) or 1 (blocked)
- Start and end are valid open cells

```python
def path_exists(maze: list[list[int]], start: tuple[int, int], end: tuple[int, int]) -> bool:
    ...
```


### Mondai 4: Count Connected Components in an Undirected Graph

You are given an undirected graph represented as an adjacency list. Each key in the graph is a node (string), and the value is a list of nodes that it is directly connected to.

Write a function that returns the number of connected components in the graph. Two nodes are in the same component if there is a path between them, directly or indirectly.

Example Input
```
graph = {
    "A": ["B"],
    "B": ["A"],
    "C": [],
    "D": ["E"],
    "E": ["D"]
}
```

Output: 3

Constraints:
- All node names are unique strings.
- The graph may be disconnected.
- It is undirected: if A connects to B, then B connects to A.

### Mondai 5: Image Fill in a 2D Grid

You are given a 2D array image of integers representing pixel values in a bitmap. Each pixel is identified by its row and column index.

Write a function that changes the color of a given starting pixel and all 4-directionally connected pixels that have the same original color to a new color.

Example Input
```
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
new_color = 2
```

Output:
```
[
    [2, 2, 2],
    [2, 2, 0],
    [2, 0, 1]
]
```


