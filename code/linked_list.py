"""Scratch pad for data structures and algorithms learning."""
import dataclasses
from typing import Any, Optional

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
    head: Node

    def insert_to_beginning(self, new_val):
        start: Node = Node(new_val, next = self.head)
        self.head = start
    
    def delete_beginning(self):
        self.head = self.head.next
    
    def insert_to_end(self, new_val):
        end = Node(new_val)
        current: Node = self.head
        while True:
            if current.next is None:
                current.next = end
                break
            current = current.next
    
    def delete_end(self):
        current: Node = self.head
        while True:
            if current.next.next is None:
                current.next = None # Chop off the end.
                break
            current = current.next
    
    def val_by_idx(self, idx: int) -> Any:
        """Get the value of the 'idx'-th node in the linked list. If 'idx' is
        invalid, returns `None`."""
        current: Node = self.head
        current_idx: int = 0 
        while True:
            if current_idx == idx:
                return current.value
            if current.next is None:
                return None
            current: Node = current.next
            current_idx += 1

    def tolist(self) -> list:
        current = self.head
        ll_aspylist: list = [self.head.value]
        while True:
            forward = current.next
            if forward is None:
                break
            ll_aspylist.append(forward.value)
            current = forward
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
    
    def create_reversed_linked_list(self):
        rev_ll = LinkedList(head = Node('d', Node('c', Node('b', Node('a')))))
        return rev_ll 
    
    def test_tolist(self):
        ll: LinkedList = self.create_linked_list()
        assert isinstance(ll.tolist(), list)

    def test__str__(self) -> str:
        ll: LinkedList = self.create_linked_list()
        return str(ll)
    
    def test_insert_to_beginning(self):
        ll: LinkedList = self.create_linked_list()
        ll.insert_to_beginning("X")
        assert ll.tolist()[0] == "X"
    
    def test_delete_beginning(self):
        ll: LinkedList = self.create_linked_list()
        head, next = ll.head, ll.head.next
        ll.delete_beginning()
        assert ll.head == next
    
    def test_insert_to_end(self):
        ll: LinkedList = self.create_linked_list()
        pass # TODO

    def test_delete_end(self):
        ll: LinkedList = self.create_linked_list()
        ll.delete_end()
        assert ll.tolist()[-1] == "c"
        rev_ll: LinkedList = self.create_reversed_linked_list()
        rev_ll.delete_end()
        assert rev_ll.tolist()[-1] == "b"

    def test_tolist(self):
        ll: LinkedList = self.create_linked_list()
        pass # TODO
        
    def test_placeholder(self):
        ll: LinkedList = self.create_linked_list()
        pass # TODO
