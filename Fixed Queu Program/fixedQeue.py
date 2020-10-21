# Fixed-Sized Queue datastructure
# supports enque and deque operations
# items are dequed in FiFo fashion
# python lists() function natively does the same thing but it is dynamically added every time list() function is called due to which this iperation is slow in python
# this programme does the same thing as list() funtion but the memory is located satically as the programme is running and active

import array
import random

class Queue:
    def __init__(self, size_max):       # size_max is the max number of elements the datastructure can store
        assert size_max > 0                 # to make sure tha the input max_size is positive
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max)) # create list of only intergers

    def empty(self):
        return self.size == 0               # returns True if size is empty

    def full(self):
        return self.size == size_max

    def enqueue(self,x):
        if self.size == self.max_size       # exits if max number of elements are reached
            return False
        self.data[self.tail] == x
        self.size += 1              # increment to signify that there is one more element now
        self.tail += 1
        if self.tail == self.max_size:
            self.tail = 0           # resets the position of tail to point again back to the first element holder
        return True                 # if enqueue operation has been successful

    def dequeue(self):
        if self.size == 0:
            return None             # if there are no elements in the Queue
        x = self.data[self.head]    # starts dequeue from the first elements onwards
        self.size -= 1              # decreaments as the size is reducing due to dequeue
        self.head += 1              # point to next item
        if self.head == self.max_size:
            self.head = 0           # after all the dequeue point the head back to first element
        return x
