from collections import deque
stack = deque()
stack.append(1)
stack.pop()

from queue import LifoQueue
stack_1 = LifoQueue(maxsize=3)


print(stack_1.get_nowait())

stack_2 = []
stack_2.append(1)
stack_2.pop()

############################
"""QUEUE"""
############################

queue1 = deque()
queue1.append(1)
queue1.popleft()

queue2 = deque()
queue2.appendleft(1)
queue2.pop()

from queue import Queue
queue3 = Queue(maxsize=3)
queue3.put(1)
queue3.get()


"""Stack using linked list"""

class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next
    
class Stack:
    def __init__(self, val, next = None):
        self.top = Node(val)
    
    def push(self, val):
        new = Node(val,self.top)
        self.top = new
        

    def pop(self):
        if self.top is not None:
            val = self.top.val
            self.top = self.top.next
            return val
        return None
    
"""Queeue Using linked list"""

class Queue:
    def __init__(self):
        self.last = None
        self.front = None

    def enqueue(self, val):
        new = Node(val)
        if self.last is None:
            self.front = self.last = new
            return
        self.last.next = new
        self.last = new

    def dequeue(self):
        if self.front is None:
            return None
        val = self.front.val
        self.front = self.front.next
        if self.front is None:
            self.last = None
        return val