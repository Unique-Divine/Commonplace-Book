"""
Q: Given an undirected graph, `graph: Dict[str, List[str]]`, and a start node,
return a list of lists, where each inner list contains the nodes at a specific
"distance" (in number of edges) from the start node.

The outer list should be ordered by distance. Nodes in each level can be in
any order.

```python
def levels(graph: Dict[str, List[str]], start: str) -> List[List[any]]:
    ...
```
"""

from collections import deque
from typing import (
    Dict, List, Tuple, Deque
)


def levels(
    graph: Dict[str, List[str]], start: str,
) -> List[List[Tuple[str, int]]]:
    if (
        start not in graph
    ):
        return [[]]

    q: Deque[Tuple[str, int]] = deque([(start, 0)])
    seen = set(start)
    out: List[List[Tuple[str, int]]] = [[]]
    while q:
        n, n_depth = q.popleft()
        if n_depth == len(out):
            out.append([])

        for child in graph.get(n, ()):
            if child in seen:
                continue
            seen.add(child)

            q.append((child, n_depth + 1))

        out[n_depth].append((n, n_depth))

    return out


def test_single_node_no_edges():
    g = {"A": []}
    out = levels(g, "A")
    assert out == [[("A", 0)]]


def test_complete_triangle():
    g = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    out = levels(g, "A")
    assert out == [
        [("A", 0)],
        [("B", 1), ("C", 1)]
    ]


def test_single_edge():
    g = {"A": ["B"], "B": ["A"]}
    out = levels(g, "A")
    assert out == [
        [("A", 0)],
        [("B", 1)]
    ]


def test_line_graph():
    g = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"]
    }
    out = levels(g, "A")
    assert out == [
        [("A", 0)],
        [("B", 1)],
        [("C", 2)],
        [("D", 3)]
    ]


def test_disconnected_graph():
    g = {
        "A": ["B"],
        "B": ["A"],
        "X": ["Y"],
        "Y": ["X"]
    }
    out = levels(g, "A")
    assert out == [
        [("A", 0)],
        [("B", 1)]
    ]


def test_isolated_start_not_in_graph():
    g = {"A": ["B"], "B": ["A"]}
    out = levels(g, "Z")
    assert out == [
        []
    ]


def test_branching_tree():
    g = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"]
    }
    out = levels(g, "A")
    # Order within levels can vary, so compare as sets
    assert [set(level) for level in out] == [
        {("A", 0)},
        {("B", 1), ("C", 1)},
        {("D", 2), ("E", 2), ("F", 2)}
    ]
