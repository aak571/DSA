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

    def delete(self, key):
        if self.root is None:
            return None
        if self.root.left is None and self.root.right is None:
            if self.root.key == key:
                self.root = None
            return

        queue = [self.root]
        key_node = None
        temp = None
        while queue:
            temp = queue.pop(0)
            if temp.key == key:
                key_node = temp
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        if key_node:
            key_node.key = temp.key
            self._delete_deepest(temp)

    def _delete_deepest(self, d_node):
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)

    def search(self, key):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.key == key:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.key, end=' ')
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    def spiral_order(self):
        if not self.root:
            return
        stack1 = [self.root]  # Right to Left
        stack2 = []  # Left to Right
        while stack1 or stack2:
            while stack1:
                temp = stack1.pop()
                print(temp.key, end=' ')
                if temp.right:
                    stack2.append(temp.right)
                if temp.left:
                    stack2.append(temp.left)
            while stack2:
                temp = stack2.pop()
                print(temp.key, end=' ')
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def find_max(self, node):
        if node is None:
            return float('-inf')
        return max(node.key, self.find_max(node.left), self.find_max(node.right))

    def find_min(self, node):
        if node is None:
            return float('inf')
        return min(node.key, self.find_min(node.left), self.find_min(node.right))

    def mirror(self, node):
        if node is None:
            return None
        node.left, node.right = self.mirror(node.right), self.mirror(node.left)
        return node