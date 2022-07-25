__author__ = "Unique Divine"
from typing import Union, List
import numpy as np
Array = np.ndarray

class TreeNode: 

    def __init__(self, data):
        self.data = data
        self.parent: 'TreeNode' = None
        self.children: List['TreeNode'] = []

    def add_child(self, child: 'TreeNode'):
        child.parent = self
        self.children.append(child)
    
    @property
    def level(self) -> int:
        level: int = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces: str = ' ' * (self.level - 1) * 3
        prefix: str = spaces + "|__" if self.parent else ""
        print(f"{prefix}{self.data}")

        if self.children:
            for child in self.children:
                child.print_tree()
    
    def __repr__(self) -> str:
        return f"TreeNode({self.data}, level={self.level})"


class Tree:
    ...


class TestTree:

    def test_placeholder(self):
        """example docstring"""

if __name__ == "__main__":
    root = TreeNode(data = "R")
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")

    a.add_child(c) # A -> C
    a.add_child(d) # A -> D

    b.add_child(e) # B -> E

    print(root.children)

    root.add_child(a)
    root.add_child(b)

    print(f"root.children: {root.children}")
    print(f"a.children: {a.children}")
    print(f"b.children: {b.children}")
    print(f"c.children: {c.children}")
    print(f"d.children: {d.children}")
    print(f"e.children: {e.children}")


    root.print_tree()