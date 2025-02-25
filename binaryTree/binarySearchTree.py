class Node:
    """A class to represent a node in the BST."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        self.root = self._insert(self.root, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def _insert(self, node, key):
        print(node)
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: Node with one or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: Node with two children, get inorder successor
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        """Find the node with the minimum value in the BST."""
        current = node
        while current.left is not None:
            current = current.left
        return current

bst = BST()
bst.insert(8)
bst.insert(4)
bst.inorder(bst.root)