from queue import Queue
class RingBuffer:
    def __init__(self, capacity ):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.cur] = item
            self.cur = (self.cur + 1) % self.capacity
        else:
            self.cur = 0
            self.data.append(item)

    def get(self):
        return self.data