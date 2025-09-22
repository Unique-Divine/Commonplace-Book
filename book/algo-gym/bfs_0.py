from typing import List, Dict, Optional, Set
from collections import deque


class MyListQueue:
    def __init__(self):
        self._q = []

    def enqueue(self, x):
        self._q.append(x)  # O(1). Adding to the end

    def dequeue(self):
        self._q.pop(0)     # O(n). Shifting


if __name__ == "__main__":

    x: deque = deque()
    print(f"type of x {type(x)}")


# ---------------- Shortest Path in an Unweighted Graph


def shortest_path_length(
        graph: Dict[str, List[str]], start: str, target: str,
) -> int:
    # Graph may be disconnected
    # All node names are lowercase strings
    # If no path exists, return -1.

    if (start not in graph) or (target not in graph):
        return -1

    visited_nodes: Set[str] = set()
    queue = deque([(start, 0)])
    while queue:
        node, path_len = queue.popleft()
        if node == target:
            return path_len
        if node in visited_nodes:
            continue
        visited_nodes.add(node)

        for neighbor_node in graph[node]:
            if neighbor_node not in visited_nodes:
                queue.append((neighbor_node, path_len + 1))

    return -1
