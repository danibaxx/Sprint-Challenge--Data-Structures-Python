class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.value = [None] * capacity
        self.pointer = 0


    def append(self, item):
        # adds given element to the buffer
        self.value[self.pointer] = item
        # print('items:' item)
        # move pointer
        self.pointer += 1
        if self.pointer == self.capacity:
            self.pointer = 0
        

    def get(self):
        # returns all elements in the buffer in given order
        # should not return none
        # return self.value
        items = []

        for i in self.value:
            if i != None:
                items.append(i)
        return items



buffer = RingBuffer(5)

print(buffer.get())

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')

print(buffer.get())

buffer.append('f')

print(buffer.get())