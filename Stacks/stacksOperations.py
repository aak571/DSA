# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# from array import array
# arr = array('i', [1, 2, 3, 4, 5])
# print(arr)


class Stack:
    def __init__(self, Max_size):
        self.stack = []
        self.max_size = Max_size

    def push(self, item):
        if self.isFull() == False:
            self.stack.append(item)
        else:
            print('Stack is full')

    def pop(self):
        if self.isEmpty() == False:
            self.stack.pop()
        else:
            print('Stack is already empty')

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def reverse(self):
        return self.stack.reverse()

    def clear(self):
        self.stack.clear()

    def isFull(self):
        if len(self.stack) == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def display(self):
        print(self.stack)

stack = Stack(5)
stack.push(12)
stack.push(15)
stack.push(36)
stack.push(87)
stack.pop()
print(stack.peek())
print(stack.size())
print(stack.reverse())
stack.clear()
stack.push(12)
stack.push(15)
stack.push(36)
stack.push(87)
print(stack.isFull())
print(stack.isEmpty())

stack.pop()
stack.push(12)
stack.push(15)
stack.push(36)
stack.push(87)
stack.push(24)
stack.push(56)

stack.display()