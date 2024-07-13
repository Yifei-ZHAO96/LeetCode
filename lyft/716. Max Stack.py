from typing import List

class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.max_stack = []

    # O(1)
    def push(self, x):
        self.stack.append(x)
        self.max_stack.append(max(x, self.max_stack[-1] if self.max_stack else x))

    # O(1)
    def pop(self):
        if len(self.stack):
            self.max_stack.pop()
            return self.stack.pop()

    # O(1) 
    def top(self):
        return self.stack[-1] if self.stack else None

    # O(1)
    def peekMax(self):
        return self.max_stack[-1] if self.max_stack else None

    # O(N)
    def popMax(self):
        max_value = self.peekMax()
        buff = []
        while self.top() != max_value:
            buff.append(self.pop())
        self.pop()
        while buff:
            self.push(buff.pop())

        return max_value

# SortedList
from sortedcontainers import SortedList
class Node:
    def __init__(self, val=-1) -> None:
        self.val = val
        self.pre = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, val):
        node = Node(val)
        pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        pre.next = node
        node.pre = pre
        return node

    def remove(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre

    def top(self):
        return self.tail.pre.val


class MaxStack(object):

    # O(1)
    def __init__(self):
        self.stack = DoublyLinkedList()
        self.max_stack = SortedList(key=lambda x: x.val)

    # O(logN)
    def push(self, x):
        node = self.stack.add(x)
        self.max_stack.add(node)

    # O(logN)
    def pop(self):
        if len(self.max_stack):
            node = self.max_stack.pop()
            self.stack.remove(node)
            return node.val

    # O(1)
    def top(self):
        return self.stack.top()

    # O(1)
    def peekMax(self):
        if self.max_stack:
            return self.max_stack[-1].val

    # O(logN)
    def popMax(self):
        if self.max_stack:
            node = self.max_stack.pop()
            self.stack.remove(node)
            return node.val