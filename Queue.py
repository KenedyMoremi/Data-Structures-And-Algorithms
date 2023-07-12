from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.appendleft(data)

    def dequeue(self):
        self.queue.pop()

        