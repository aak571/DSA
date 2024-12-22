class Queue:
    def __init__(self):
        self.queue = []
        self.max_size = 5
        # print(self.queue, self.max_size)

    def enqeue(self, item):
        if self.isFull() == False:
            self.queue.append(item)
        else:
            print('The Queue is full')
        # print(self.queue.index(item))

    def dequeue(self):
        if self.isEmpty() == False:
           self.queue.pop(0) #  [10, 20, 30] -> [20, 30]
        else:
            print('There is nothing in the Queue to remove !!!')
        # print(self.queue.index(20))

    def display(self):
        return self.queue

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def contains(self, item):
        return item in self.queue

    def isFull(self):
        return len(self.queue) == self.max_size

    def isEmpty(self):
        return len(self.queue) == 0

queueObj = Queue()
queueObj.enqeue(10)
queueObj.enqeue(20)
queueObj.enqeue(30)
queueObj.enqeue(40)
queueObj.enqeue(50)
queueObj.dequeue()
print(queueObj.peek())
print(queueObj.size())
queueObj.clear()
print(queueObj.contains(20))
print(queueObj.isFull())
print(queueObj.isEmpty())
print(queueObj.display())
queueObj.dequeue()

# queueObj.dequeue()
# queueObj.dequeue()
# queueObj.dequeue()
# queueObj.dequeue()
# queueObj.dequeue()
# queueObj.dequeue()
# print(queueObj.display())