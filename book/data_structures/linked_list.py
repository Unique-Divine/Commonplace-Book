"""Scratch pad for data structures and algorithms learning."""
import dataclasses
from typing import Any, Optional, Union, List

@dataclasses.dataclass
class Node:
    """Node of a singly linked list."""
    value: Any
    next: Optional['Node'] = None

"""
class Node: # Equivalently, 
    def __init__(self, 
                 value,
                 next: Optional['Node'] = None):
        self.value = value
        self.next = next
"""

import dataclasses
from typing import Any, Optional

@dataclasses.dataclass
class DLNode:
    """Node of a doubly linked list."""
    value: Any
    next: Optional['DLNode'] = None
    prev: Optional['DLNode'] = None

@dataclasses.dataclass
class LinkedList:
    head: Optional[Node] = None

    def insert_at_beginning(self, value):
        start: Node = Node(value, next = self.head)
        self.head = start

    def append(self, value):
        if not self.head:
            self.head = Node(value)

        curr: Node = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    def insert_at_idx(self, value: Any, idx: int):
        if idx == 0:
            self.head = Node(value, next = self.head)
        curr: Node = self.head
        curr_idx: int = 0
        while curr.next:
            if curr_idx + 1 == idx:
                curr.next = Node(value, next = curr.next)
                break
            curr = curr.next
            curr_idx += 1
    
    def delete_beginning(self):
        self.head = self.head.next
    
    def delete_end(self):
        if not self.head:
            return None
        curr: Node = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None # Chop off the end.
    
    def delete_at_idx(self, idx: int):
        if not self.head:
            return None
        if idx == 0:
            self.head = self.head.next

        curr_idx: int = 0 
        curr: Node = self.head
        
        while curr.next:
            if curr_idx + 1 == idx:
                curr.next = curr.next.next
                break
            curr = curr.next
            curr_idx += 1
    
    def get_node(self, idx: int) -> Union[Node, None]:
        """Get the 'idx'-th node in the linked list. If 'idx' is
        invalid, returns `None`."""
        
        if not self.head:
            return None
        if idx == 0:
            return self.head

        curr: Node = self.head
        curr_idx: int = 0 
        if curr_idx + 1 == idx:
            return curr.next

        while curr.next:
            if curr_idx + 1 == idx:
                return curr.next
            curr = curr.next
            curr_idx += 1
        if (curr.next is None) and (idx == -1):
            return curr

    def get_value(self, idx: int) -> Any:
        """Get the value of the 'idx'-th node in the linked list. If 'idx' is
        invalid, returns `None`."""

        idx_node: Node = self.get_node(idx=idx)
        if idx_node:
            return idx_node.value

    def get_tail(self) -> Node:
        tail: Node = self.get_node(-1)
        return tail

    def tolist(self) -> list:
        curr = self.head
        ll_aspylist: list = [self.head.value]
        while True:
            forward = curr.next
            if forward is None:
                break
            ll_aspylist.append(forward.value)
            curr = forward
        return ll_aspylist

    def __str__(self) -> str:
        ll_aspylist: list = self.tolist()
        return str(ll_aspylist)
    
    def __repr__(self) -> str:
        return str(self)

class TestLinkedList:

    def create_linked_list(self) -> LinkedList:
        ll = LinkedList(head = Node('a', Node('b', Node('c', Node('d')))))
        return ll
    
    def create_reversed_linked_list(self) -> LinkedList:
        rev_ll = LinkedList(head = Node('d', Node('c', Node('b', Node('a')))))
        return rev_ll 
    
    def create_empty_linked_list() -> LinkedList:
        empty_ll = LinkedList(head = None)
        return empty_ll

    
    def test_tolist(self):
        ll: LinkedList = self.create_linked_list()
        assert isinstance(ll.tolist(), list)

    def test__str__(self) -> str:
        ll: LinkedList = self.create_linked_list()
        return str(ll)
    
    def test_insert_at_beginning(self):
        ll: LinkedList = self.create_linked_list()
        ll.insert_at_beginning("X")
        assert ll.tolist()[0] == "X"
    
    def test_append(self):
        ll: LinkedList = self.create_linked_list()
        rev_ll: LinkedList = self.create_reversed_linked_list()
        for linkedlist in [ll, rev_ll]:
            linkedlist.append("e")
            assert "e" == linkedlist.tolist()[-1]
            assert "e" == linkedlist.get_value(idx = -1)
            linkedlist.append("special")
            assert "special" == linkedlist.tolist()[-1]
            assert "special" == linkedlist.get_value(idx = -1)

    def test_insert_at_idx(self):
        insert_val: str = "X"
        insert_indices: List[int] = [0, 2, 1, 3]
        for insert_idx in insert_indices: # type: int
            ll: LinkedList = self.create_linked_list()
            ll.insert_at_idx(value = insert_val, idx = insert_idx)
            assert ll.tolist()[insert_idx] == insert_val, f"{ll}"
        
        # Index outside length of the linked list
        before: list = ll.tolist()
        ll.insert_at_idx(insert_val, idx = 20)
        after: list = ll.tolist()
        assert before == after

    def test_delete_beginning(self):
        ll: LinkedList = self.create_linked_list()
        head, next = ll.head, ll.head.next
        ll.delete_beginning()
        assert ll.head == next

    def test_delete_end(self):
        ll: LinkedList = self.create_linked_list()
        ll.delete_end()
        assert ll.tolist()[-1] == "c"
        rev_ll: LinkedList = self.create_reversed_linked_list()
        rev_ll.delete_end()
        assert rev_ll.tolist()[-1] == "b"

    def test_delete_at_idx(self):
        ll: LinkedList = self.create_linked_list()
        pass # TODO

    def test_get_node(self):

        ll: LinkedList = self.create_linked_list()
        node0 = ll.get_node(idx = 0)
        assert node0 == ll.head
        node1 = ll.get_node(idx = 1)
        assert node1 == ll.head.next
        node2 = ll.get_node(idx = 2)
        assert node2 == ll.head.next.next
        node3 = ll.get_node(idx = 3)
        assert node3 == ll.head.next.next.next
        node_end = ll.get_node(idx = -1)
        assert node_end == ll.head.next.next.next
        assert node_end == node3

        rev_ll: LinkedList = self.create_reversed_linked_list()
        node0 = rev_ll.get_node(idx = 0)
        assert node0 == rev_ll.head
        node1 = rev_ll.get_node(idx = 1)
        assert node1 == rev_ll.head.next
        node2 = rev_ll.get_node(idx = 2)
        assert node2 == rev_ll.head.next.next
        node3 = rev_ll.get_node(idx = 3)
        assert node3 == rev_ll.head.next.next.next
        node_end = rev_ll.get_node(idx = -1)
        assert node_end == rev_ll.head.next.next.next
        assert node_end == node3

    def test_get_value(self):
        ll: LinkedList = self.create_linked_list()
        assert "a" == ll.get_node(idx = 0).value
        assert "b" == ll.get_node(idx = 1).value
        assert "c" == ll.get_node(idx = 2).value
        assert "d" == ll.get_node(idx = 3).value
        assert "d" == ll.get_node(idx = -1).value

        rev_ll: LinkedList = self.create_reversed_linked_list()
        assert "d" == rev_ll.get_node(idx = 0).value
        assert "c" == rev_ll.get_node(idx = 1).value
        assert "b" == rev_ll.get_node(idx = 2).value
        assert "a" == rev_ll.get_node(idx = 3).value
        assert "a" == rev_ll.get_node(idx = -1).value

    def test_get_tail(self):
        ll: LinkedList = self.create_linked_list()
        assert ll.get_tail() == ll.head.next.next.next
        rev_ll: LinkedList = self.create_reversed_linked_list()
        assert rev_ll.get_tail() == rev_ll.head.next.next.next

    def test_placeholder(self):
        ll: LinkedList = self.create_linked_list()
        pass # TODO