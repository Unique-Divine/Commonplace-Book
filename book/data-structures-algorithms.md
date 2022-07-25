<!-- data-structures-algorithms.md -->

***

## Data Structures & Algorithms (DSA)

***

Algorithm : A fancy word for a simple thing: A program that solves a problem.

Topics

* Linked lists, arrays, stacks, queues
* Sorting: Insertion sort, merge sort, divide and conquer, quicksort, counting sort, Radix sort
* Heaps, heapsort
* Binary search trees, Red-black trees
* Graphs, Breadth-first search, Depth-first search
* Shortest paths, Negative cycles, All-pairs shortest paths
* Hashing, hash tables, dictionaries
* NP-Completeness
* Greedy algorithms
* Dynamic programming

Introduction to Algorithms by Thomas H Cormen, Charles E Leiserson, buncha others (third edition)

**Why study data structures and algorithms (DSA)?**

[Role of DSA in Programming (July, 2020)](https://blog.codechef.com/2020/07/24/the-role-of-data-structure-and-algorithms-in-programming/)

***

### List-Based Collections

***

#### Arrays and Python Lists

We can broadly define a **collection** as a group of things. A list (`CSList`) is a kind of collection with a few properties.

1. Lists are ordered.
2. Elements of a list can have various types.
3. Lists are fully mutable and have no fixed length, thus insert, delete, replace/swap, and concatenate/append are all viable operations.

In computer science, arrays are an implementation of a list with additional constraints, i.e.

```python
class CSArray(CSList):
    ...
```

An **array** (`CSArray`) is an ordered collection of elements that each have an address called an index.

* In some languages, arrays must contain elements of the same type. Q: Why? A: Memory is often pre-allocated for arrays.
* Arrays often have a set size upon creation rather than being described just by a starting point (like linked lists and stacks).

Q: What key factor differentiates arrays from lists? A: Arrays store a location for each element as a number. That number is called an index.

**Ex. Pivot Index | **[**leetcode**](https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/)**:**

You are given an integer array, `nums`, where the largest integer is unique. Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the alrgest element. Otherwise, return `-1`.

```python
def dominant_idx(nums: list[int]) -> int:
    if not nums:
        return -1
    max_val: int = max(nums)
    max_val_idx: int = nums.index(max_val)
    for i, num in enumerate(nums):
        if i == max_val_idx:
            continue
        if max_val < num * 2:
            return -1
    return max_val_idx
```

**Ex. Diagonal Traverse | **[**leetcode**](https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/)

Given an m by n matrix `mat`, return an array of all the elements of the array in the following diagonal order.

![](code/img/code-array-diagonal-traverse.png)

**Python Lists**

```python
class PyList(CSArray):
    """Python lists""" ...
```

Inserting into a PyList is $O(n)$. Q: Why? → A Python list is really a CSArray. It has indices and inserting requires shifting up to $n$ values.

Retrieving an alement from a PyList is $O(1)$, or "constant time". Q: Why? → It's indexed. A PyList is a CSArray.

```python
ell: PyList # Given ell
>>> len(ell)
n
>>> import copy
>>> ell.copy()      # O(n) -> Copying n elements
>>> ell.append(...) # O(1) -> Doesn't require changing the other values
```

```python
idx: int 
item: Any
>>> ell.insert(idx, item)  # O(n) -> Worst case, you have to shift n items
>>> ell[idx]               # O(1) -> Retrieval
>>> del ell[idx]           # O(n) -> Deleting changes up to n indices
```

Deleting an element changes all of the indices following that position. Thus, deletion can cause up to $n$ re-writes.

A for loop through `ell` is $O(n)$ because there are $n$ iterations.

Slices

1. Get
2. Delete
3. Set

#### Linked lists

Python lists aren't lists in the traditional computer science sense. That would be a linked list. A **linked list** is a data structure consisting of a collection of nodes which together represent a sequence.

* Linked lists are ordered like arrays, but there are no indices. The order is purely kept by the links.
* Each node is unaware of its location in the linked list because it's unindexed. The nodes are also unaware of how long the list is.

A **singly linked list** is a sequence of **nodes**. Each node in a singly linked list holds a value and keeps reference to the next node. This reference is the single link.

Q: Implement a `dataclass` for a node of a **singly** linked list.

```python
import dataclasses
from typing import Any, Optional

@dataclasses.dataclass
class Node:
    """Node of a singly linked list."""
    value: Any
    next: Optional['Node'] = None
```

A **doubly linked list** is a sequence of nodes that each hold a value and keep a reference to both the previous and next node.

Q: Implement a `dataclass` for a node of a **doubly** linked list.

```python
import dataclasses
from typing import Any, Optional

@dataclasses.dataclass
class DLNode:
    """Node of a doubly linked list."""
    value: Any
    next: Optional['DLNode'] = None
    prev: Optional['DLNode'] = None
```

* [ ] Q: Similar to the array, the linked list is a linear data structure. What makes it linear?

The **head node** of a linked list is the first, or outermost, node. Singly and doubly linked lists can be implemented based just on the head node.

Q: Write a method-less class for a singly linked list.

```python
@dataclasses.dataclass
class Node:
    value: Any
    next: Optional['Node'] = None

@dataclasses.dataclass
class LinkedList:
    head: Node

    # ... methods
```

Q: Using the above `LinkedList` and `Node` classes, create a linked list instance that describes `"a" → "b" → "c"`, where arrows represent the node pointers and the letters represent values.

```python
ll = LinkedList(head = Node('a', Node('b', Node('c'))))
```

Q: Insert an element at the beginning of a linked list.

**Time complexity of insert and delete**

* Delete @ beginning of a linked list: $O(1)$.
* Delete @ end: $O(n)$
* Delete @ a given index: $O(n)$. At worst, you have to visit $n$ nodes.
* Insert @ beginning: $O(1)$.
* Insert @ end: $O(n)$.
* Insert @ idx: $O(n)$.

To traverse a linked list, you have to start from the head. Traversing has $O(n)$ time compelxity because there are $n$ references to go through.

#### Stacks

Stacks are also list-based data strucures. Imagine a stack of pancakes. You can keep stacking elements on top and have easy access to the top-most element.

Adding an element to a stack is called **pushing** and taking an element from the top of a stack is called **popping**. Both `Stack.pop` and `Stack.push` are $O(1)$ (constant time).

The value and pointers of the elements aren't specified by a stack, meaning that stacks can actually be implemented as linked lists, where the top of the stack is the head of a singly linked list. It just needs to have methods for adding and removing elements.

You may see the notation L.I.F.O. associated with stacks. It stands for "Last In, First Out". The last element pushed is the first one popped.

Python lists (PyList) have stack functionality built in with `PyList.pop()` and `PyList.append()`.

#### Queues

Queues are similar to stacks, except they are are "first in, first out" (FIFO).

Terminology:

* enqueue(): Adding on to the end of the queue.
* dequeue(): Removing an item from the front of the queue.

Queues are used for breadth-first search, whereas stacks are used for depth-first search.

### Trees

A tree is basically an extension of a linked list. A linked list has a head node that may have a pointer to the next node. The first element of a tree is called the **root**.

Each element of a tree holds some data. The elements of a tree are often called **nodes**.

Properties

1. A tree must be connected. Starting from the root, there must be some path to reach every node in the tree.
2. There must not be any cycles. A cycle is present when there's a way to encounter the same node twice.
   * If A, B, and C are nodes of a tree, we can't have A → B, B → C, and C → A, for example.

Terminology:

1. Edges, path: The connections between nodes are called **edges**. A group of edges is called a **path**.
2. The nodes at the end, or bottom, of a tree are called **leaves**, or **external nodes**.
3. Level and depth: The **level** of a node, `level: int = connections_to_root + 1`, where `connections_to_root` is the number of pointers between the given node and the root of the tree. Thus, the root is level one and nodes immediately connected to it are on level two.
   * **Depth** of a node: Number of edges between a node and the root of the tree. Thus, `level = depth + 1`.
4. Nodes in a tree have their pointer(s) described in terms of a parent-child relationship. If nodes $N\_1$ and $N\_2$ are such that $N\_1 → N\_2$, then we say $N\_1$ is the **parent** and $N\_2$ is the **child**.
   * A node in the body of the tree can be both a parent and a child. It just depends what it points to. The root is only a parent.
   * Each child can only have one parent. Why? Having two would violate the cycle property.
   * If a parent node has multiple children, those children are considered **siblings**.
   * A node at a lower level than another is called a **descendant**. A node at a higher level than another is called an **ancestor**.
5. **Height** of a node: Number of edges between a node and the deepest leaf that's connected to the node. A leaf has height 0.
   * The **height of a tree** is the height of its root node. The height of a tree is also equivalent to the maximum depth of the nodes in the tree.

Cloze:

![](code/img/tree-terminology-udacity.png)- Level of D? 3 - Height of B? 2 - Depth of F? 3 Node B: height 2 Node D: height 0, depth 2, Node E: height 1 Node F: height 0, depth 3,

**Tree Traversal**

There are two main approaches to tree traversal: Depth first search (DFS) and breadth first search (BFS)

The idea behind DFS is to prioritize traversing child nodes.

In BFS, each node of a level is traversed recurrently before visiting children in the next level.

**Level order traversal** is an example of a breadth first search. It's described as follows:

**Depth-First Traversals**

**1. Pre-Order Traversal**

In pre-order traversal, you count a node as traversed a node as soon as you reach it before traversing further. Keep in mind that other methods may involve counting a node as traversed only _after_ you've traversed all of its children.

Pre-Order Traversal Algorithm

1. Start at the root and immediately check it off as seen.
2. Pick one of the root's children, normally the left child by convention, and check it off too.
3. Continue traversing down the left children and checking them off until you hit a leaf.
4. Check off the leaf, `leaf0`, and go back to its parent. Now, traverse to the sibling just to the right of `leaf0` and check it off too (if it exists).
5. Continue this pattern (step 3 and 4) of prioritizing left children in the traversal until "go back its parent" leads leads you to the root.
6. Pick the next child of the root and repeat this pattern of left child prioritization.

![](code/img/tree-diagram-example.png)

This algorithm would give the following traversal on the above example:\
A, B, E, F, I, C, G, H, J, D

**2. In-Order Traversal**

In-order traversal is another type of depth-first search. Because of this, we still need to explore all of the children first, so we'll visit the nodes in the same path as in pre-order traversal, however we'll now _check off_ the nodes in a different order. We only check off a node once we've seen its left child and come back to the parent.

![](code/img/tree-diagram-example.png)

In-order traversal on the tree above:\
E, B, I, F, , G

TODO: Don't really understand this

**3. Post-Order Traversal**

![](code/img/tree-terminology-udacity.png)

Traversal: D, F, E, B, C, A

![](code/img/tree-diagram-example.png)

Post-order traversal on the tree above:\
E, I, F, B, G, J, H, C, D, A

#### Binary Trees

Binary trees are trees with nodes that can have at most two children.

Binary trees don't have any order by which we can search or sort. Consequently, there's no trick to searching for an element faster than linear time. **Searching for an element/node** in a binary tree is an $O(n)$ operation, where $n$ is the number of nodes in the tree.

Operations to implement:

* Search
* Insert
* Delete

#### Binary Search Tree (BST)

***

### Searching and Sorting

#### Binary search

Suppose you have an array sorted in numerical order. If you want to check whether a number, `search_value`, exists in the array, you could start at the front and check every element, and this could be $O(n)$ if the number is large and close to $O(1)$ if the number is small.

With binary search, you can take advantage of the fact the array is sorted. Compare the `search_value` with the middle element of the array. If `search_value` is bigger, you only need look at the half of the array with bigger values. You can keep bisecting the these subsections of that array and comparing with the middle element reduce the search space.

Cloze:

* The main constraint for binary search is that the elements of the array need to be sorted.
* Binary search time complexity is $O(\log\_2(n) + 1) \to O(\log\_2(n))$, where $n$ is the array length.

***

**DSA Resources:**

* Python implementations of tons of algorithms: https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md
* Udacity course: https://classroom.udacity.com/courses/ud513/lessons/7174469398/concepts/71201055390923
* Python Algorithms book
