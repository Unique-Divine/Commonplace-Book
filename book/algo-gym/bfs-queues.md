# Breadth-First Search and Queues

Absolutely — here are short, focused Python practice questions related to **queues**, designed to test:

* understanding of the data structure
* algorithm usage
* complexity analysis
* and rationale behind implementation choices

## Problem Solving Tracker
- [x] [Q1: Enqueue and Dequeue (Basic Ops)](#q1-enqueue-and-dequeue-basic-ops)
- [x] [Q2: O(1) vs O(n) Trap](#q2-o1-vs-on-trap)
- [x] [Q3: BFS with a Queue](#q3-bfs-with-a-queue)
- [x] [Q4: Queue implemented with Stacks](#q4-queue-implemented-with-stacks)

---

## Q1: Enqueue and Dequeue (Basic Ops)

**Question:**
Implement a simple queue using Python’s built-in `list`. Your queue must support `enqueue(x)` and `dequeue()` methods. What are the time complexities of each?

```python
class MyQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        """Adds to the queue"""

    def dequeue(self):
        """Retrieves the oldest value from the queue."""
```

**Answer:**

```python
class MyListQueue:
    def __init__(self):
        self._q = []

    def enqueue(self, x):
        self._q.append(x)  # O(1). Adding to the end

    def dequeue(self):
        self._q.pop(0)     # O(n). Shifting
```

* `enqueue` using `append(x)` is O(1)
* `dequeue` using `pop(0)` is O(n) due to shifting
* Better to use `collections.deque`

Q: What is the time complexity of `List.pop()`? 

O(1). Removing from the back.

Q: What is the time complexity of `List.pop(i)`, where `i` is some index of the
list?

O(n). Shifting of all elements from `i` onward. The worst case is `List.pop(0)`,
where we'd have to move everything.

## Q2: O(1) vs O(n) Trap

**Question:**
What is the time complexity of this operation?

```python
queue = []
for i in range(1000):
    queue.append(i)

while queue:
    queue.pop(0)
```

**Follow-up:**

> Rewrite it to make both insertion and removal O(1).

**Answer:**

```python
from collections import deque
queue: deque[int] = deque()
for i in range(1000):
    queue.append(i)

while queue:
    queue.popleft()
```

* The loop of `pop(0)` makes it **O(n²)** total.
* Replace `queue = []` with `deque()` and `pop(0)` with `popleft()`.

**Answer:**
✅ **B. `deque`**

## Q3: BFS with a Queue

**Question:**
Below is incomplete logic for breadth-first search (BFS) traversal of a
graph. The graph is implemented as a map to an adjacency list.

Q: If the nodes are strings, What type does the graph have?
```python
graph: Dict[str, List[str]]
```

Q: How do you intialize the queue for BFS, given some starting node, `start`?
```python
from collections import deque

queue = deque([start])
```

Q: Does BFS travel require a visited set?

Yes, it's necessary to avoid cycles and redundant processing.

Q: Will BFS traversal touch nodes disconnected from a given starting node,
`start`? 

No, `bfs(graph, start)` only traverses nodes reachable from `start` in `graph`.

Q: How can you guarantee you've traversed a full graph if there are disconnected
nodes?

Loop over all nodes and call BFS on each unvisited one.

Q: Implement this BFS traversal, given that the graph has type 
`Dict[str, List[str]]`.

```python
from collections import deque
from typing import List, Dict, Deque, Set

def bfs(graph: Dict[str, List[str]], start: str) -> Set[str]:
    visited: Set[str] = set()
    queue: Deque[str] = deque([start])
    
    while queue:
        node: str = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        queue.extend(graph[node]) # Add neighbors to queue.

    return visited
```

Q: To add a single item to a `Deque` in Python, we use what function?
Q: To add a multipe items to a `Deque` in Python, we use what function?
```
deque.append(item: T)
deque.extend(items: Iterable[T])
```

Q: To grab the oldest value from a `Deque` in Python, use what function?
```
deque.popleft
```

**Follow-up:**

> What is the time complexity of BFS in terms of nodes `n` and edges `e`?

**Answer:**

* Fill-in: `queue.extend(graph[node])`
* Time complexity: **O(n + e)**

## Q4: Queue implemented with Stacks 

Implement a first in first out (FIFO) queue using only two stacks. The
implemented queue should support all the functions of a normal queue (push, peek,
pop, and empty).

Implement the MyQueue class:
- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns true if the queue is empty, false otherwise.

Notes:
- You must use only standard operations of a stack, which means only push to top,
peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may
simulate a stack using a list or deque (double-ended queue) as long as you use
only a stack's standard operations.


```python
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """Add to the queue"""
        self.input.append(x)

    def pop(self) -> int:
        """Get the next element in the queue and remove it"""
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        """View the next element in the queue"""
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """Returns True if the queue is empty"""
        return not self.input and not self.output
```

## Q5: Shortest Path in an Unweighted Graph

Q: You are given an undirected, unweighted graph as an adjacency list and two nodes
`start` and `target`. 

Implement a function that returns the **shortest path** from `start` to `target`
as a list of nodes. If no path exists, return `None`.

Implement a function that returns the shortest distance between `start` and
`target`, where distance is the number of edges in the shortest path. Return `-1`
if `target` is unreachable.

**Example**

```
graph = {
  "A": ["B", "D"],
  "B": ["A", "C"],
  "C": ["B", "D"],
  "D": ["A", "C", "E"],
  "E": ["D"]
}
start = "A", target = "E"

Output (path): ["A", "D", "E"]
Output (distance): 2
```

**Constraints**

* `1 <= |V| <= 2 * 10^5`
* `0 <= |E| <= 4 * 10^5`
* Node labels are hashable and comparable
* Adjacency may be sparse; neighbors may be empty
* Graph may be disconnected

Approach (BFS, unweighted):
* Use BFS from `start`.
* Track a `parent` map to reconstruct the path when `target` is first seen.
* Mark `visited` as soon as nodes are enqueued to avoid duplicates.
* Distance equals BFS level count, or the length of the reconstructed path minus one.

**Correctness sketch**
In an unweighted graph, BFS explores nodes in nondecreasing distance from `start`.
When `target` is dequeued the first time, the discovered tree depth equals the shortest number of edges.
The `parent` map yields a simple path of that length.

**Complexity**
Time: `O(V + E)`
Space: `O(V)`

Implementation (typed, Pythonic)


Notes and pitfalls:
- Enqueue neighbors and mark `visited` **at enqueue time**, not dequeue time, to
avoid multiple enqueues.
- If the graph is directed, do not add reverse edges. The code still works as
long as the adjacency reflects direction.
- For very large inputs, prefer `tuple` or `list` neighbors and avoid repeated
`in` checks on long sequences. The above uses `visited` as a `set` which is
`O(1)` average.
- If the node space is dense and integer-indexed, an array of parents and a
`deque[int]` can be faster, but the generic typed version above is flexible and
clean.

If you want, we can add a variant that returns *all* shortest paths, or a multi-source BFS.


## Q6: Level-Order Traversal 

Q: Given an undirected graph, `graph: Dict[str, List[str]]`, and a start node,
return a list of lists, where each inner list contains the nodes at a specific
"distance" (in number of edges) from the start node.

The outer list should be ordered by distance. Nodes in each level can be in any order.

```python
def levels(graph: Dict[str, List[str]], start: str) -> List[List[str]]:
    ...
```

(Graph BFS by Depth)

Q: Why is a BFS a natural fit for an algorithm to solve this problem?

The problem talks about grouping nodes in a  graph based on how far they are from
a starting node. It looks for a shortest possible route (distance). BFS explores
nodes in waves, all nodes at distance 1, then distance 2, 3, and so on.

Question: 

 Do we need to label the levels of nodes that are parents of the `start`, or only children of `start`? Like if A -> B - > C and C is the start, would A be included in the output? 


