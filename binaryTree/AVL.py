class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at height 1

class AVLTree:
    # Get height of node
    def get_height(self, node):
        return node.height if node else 0

    # Get balance factor
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Right Rotate (LL Case)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x  # New root after rotation

    # Left Rotate (RR Case)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # New root after rotation

    # Insert a key into AVL Tree
    def insert(self, node, key):
        # Normal BST insertion
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Update height of current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get balance factor
        balance = self.get_balance(node)

        # Perform rotations if unbalanced
        # Left Heavy (LL Case)
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Heavy (RR Case)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left-Right (LR Case)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left (RL Case)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node  # No rotation needed

    # Get the node with minimum value
    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # Delete a node from AVL Tree
    def delete(self, node, key):
        # Standard BST delete
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Node with two children: Get inorder successor
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        # If tree has only one node
        if not node:
            return node

        # Update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get balance factor
        balance = self.get_balance(node)

        # Balance tree
        # Left Heavy (LL Case)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # Right Heavy (RR Case)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # Left-Right (LR Case)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left (RL Case)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Preorder Traversal (Root, Left, Right)
    def pre_order(self, node):
        if node:
            print(node.key, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

# Driver Code
avl_tree = AVLTree()
root = None

# Insert nodes
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl_tree.insert(root, key)

print("Preorder traversal after insertion:")
avl_tree.pre_order(root)
print()

# Delete a node
root = avl_tree.delete(root, 20)
print("Preorder traversal after deletion of 20:")
avl_tree.pre_order(root)
