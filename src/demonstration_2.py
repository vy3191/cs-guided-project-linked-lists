"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
from _typeshed import NoneType


class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # Your code here
    current_node = head_of_list
    previous_node = None
    next_node = None​
    while current_node:
        # set the next_node, preserving access
        next_node = current_node.next​
        # make current node, point to previous node
        current_node.next = previous_node​
        # Shift the current and previous pointers to the right
        previous_node = current_node
        current_node = next_node​
    return previous_node


head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)