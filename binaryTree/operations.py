class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        queue = [self.root]
        while queue:  # empty list = False
            temp = queue.pop(0)
            if not temp.left:
                temp.left = Node(key)
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = Node(key)
                return
            else:
                queue.append(temp.right)