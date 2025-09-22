"""
## Q5: Shortest Path in an Unweighted Graph

Q: You are given an undirected, unweighted graph as an adjacency list and two
nodes `start` and `target`.

Implement a function that returns the **shortest path** from `start` to `target
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
"""
from __future__ import annotations
import pytest

from collections import deque
from typing import (
    Deque, Dict, List, Optional, Sequence, Set,
)

N = str
Graph = Dict[N, Sequence[str]]


def shortest_path(graph: Graph[N], start: N, target: N) -> Optional[List[N]]:
    """Return a shortest path from start to target as a list of nodes, or None
    if unreachable.

    BFS on an unweighted graph guarantees optimality by edge count.
    """
    if start == target:
        return [start]
    if (
        start not in graph
    ):
        return None

    q: Deque[N] = deque([start])
    visited: Set[N] = {start}
    parent_of: Dict[N, N] = {}

    while q:
        u: N = q.popleft()
        for v in graph.get(u, ()):
            if v in visited:
                continue
            visited.add(v)

            parent_of[v] = u
            if v == target:
                # Reconstruct path
                path: List[N] = [v]
                while path[-1] != start:
                    path.append(parent_of[path[-1]])
                path.reverse()
                return path
            q.append(v)

    return None


def shortest_distance(graph: Graph[N], start: N, target: N) -> int:
    """
    Return the number of edges in the shortest path from start to target,
    or -1 if unreachable.
    """
    if start == target:
        return 0
    if start not in graph:
        return -1

    q: Deque[N] = deque([start])
    visited: Set[N] = {start}
    # You can carry depth per node or use a sentinel per level.
    # Per-node is simpler.
    depth_of: Dict[N, int] = {start: 0}

    while q:
        q_n = q.popleft()
        q_n_depth = depth_of[q_n]
        for child in graph.get(q_n, ()):
            if child in visited:
                continue
            visited.add(child)

            depth_of[child] = q_n_depth + 1
            if child == target:
                return depth_of[child]

            q.append(child)

    return -1


@pytest.fixture(scope="module")
def G() -> Graph[str]:
    return {
        "A": ("B", "D"),
        "B": ("A", "C"),
        "C": ("B", "D"),
        "D": ("A", "C", "E"),
        "E": ("D",),

        # Disconnected component
        "X": ("Y",),
        "Y": ("X", "Z"),
        "Z": ("Y",),

        # Node referenced as a neighbor but *not* present as a key
        # (tests .get default)
        "M": ("N",),  # N is missing from keys
    }


# --- Core correctness --------------------------------------------------------

def test_basic_path(G):
    # A -> E has at least one shortest path of length 2: A-D-E
    path = shortest_path(G, "A", "E")
    assert path is not None
    assert path[0] == "A" and path[-1] == "E"
    assert len(path) - 1 == 2  # distance by edges
    assert shortest_distance(G, "A", "E") == 2


def test_multiple_shortest_paths(G):
    # A -> C can be A-B-C or A-D-C (both length 2)
    path = shortest_path(G, "A", "C")
    assert path is not None
    assert path[0] == "A" and path[-1] == "C"
    assert len(path) - 1 == 2
    # distance should match
    assert shortest_distance(G, "A", "C") == 2


def test_start_equals_target(G):
    assert shortest_path(G, "A", "A") == ["A"]
    assert shortest_distance(G, "A", "A") == 0


def test_unreachable_across_components(G):
    # A is disconnected from X/Y/Z
    assert shortest_path(G, "A", "Z") is None
    assert shortest_distance(G, "A", "Z") == -1


def test_missing_keys_are_safe(G):
    # G["M"] includes neighbor "N" which is *not* a key in the mapping.
    # BFS should not crash: it treats "N" as a node with zero neighbors.
    # M -> N is a path of length 1, even though N has no adjacency entry.
    path = shortest_path(G, "M", "N")
    assert path == ["M", "N"]
    assert shortest_distance(G, "M", "N") == 1


def test_unknown_nodes_return_none_or_minus_one(G):
    assert shortest_path(G, "UNKNOWN", "A") is None
    assert shortest_path(G, "A", "UNKNOWN") is None
    assert shortest_distance(G, "UNKNOWN", "A") == -1
    assert shortest_distance(G, "A", "UNKNOWN") == -1
