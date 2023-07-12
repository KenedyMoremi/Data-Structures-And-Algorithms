from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()

    def add(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

        