class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = []

    def append(self, item):
        # adds given element to the buffer
        self.capacity += 1
        self.value.append(item)

    def get(self):
        # returns all elements in the buffer in given order
        # should not return none
        if self.capacity == None:
            return False
        else:
            return self.capacity

buffer = RingBuffer(5)

buffer.get()

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')

buffer.get()

buffer.append('f')