class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current < len(self.storage):
            self.storage[self.current] = item
            self.current += 1
        else:
            self.current -= self.capacity
            self.storage[self.current] = item
            self.current += 1
        return self.storage

    def get(self):
        return [x for x in self.storage if x is not None]


buffer = RingBuffer(3)

print(buffer.get(), '-------> []')  # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get(), '-------> a, b, c')   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
print(buffer.get(), ' -------> d, b, c')   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get(), ' -------> d, e, f')  # should return ['d', 'e', 'f']
