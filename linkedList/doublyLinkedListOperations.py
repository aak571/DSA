class Node:
    """Class to represent a node in the doubly linked list."""
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    """Class to represent the doubly linked list."""
    def __init__(self):
        self.head = None  # Pointer to the head of the list

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_after(self, prev_data, data):
        """Insert a node after a given node in the list."""
        temp = self.head
        while temp and temp.data != prev_data:
            temp = temp.next
        if not temp:
            print("Node with data not found.")
            return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_node(self, data):
        """Delete a node by value."""
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        # If the node to be deleted is the head
        if temp.data == data:
            if temp.next:
                temp.next.prev = None
            self.head = temp.next
            print(f"Deleted node with data {data}.")
            return
        while temp and temp.data != data:
            temp = temp.next
        if not temp:
            print("Node with data not found.")
            return
        # Re-link the previous and next nodes
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def traverse_forward(self):
        """Traverse the list forward and print the elements."""
        temp = self.head # self.tail
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next  # temp.prev
        print("List (Forward):", elements)

    def traverse_backward(self):
        """Traverse the list backward and print the elements."""
        temp = self.head
        if not temp:
            print("The list is empty.")
            return
        while temp.next:
            temp = temp.next
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.prev
        print("List (Backward):", elements)

