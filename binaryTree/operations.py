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

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))