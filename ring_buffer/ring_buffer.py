class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        if len(self.storage) == self.capacity:
          self.storage.pop(0)
          self.storage.append(item)
        else:
          self.storage.append(item)

    def get(self):
        return self.storage