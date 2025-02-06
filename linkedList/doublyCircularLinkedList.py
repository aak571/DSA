class Node:
    def __init__(self, Data):
        self.data = Data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # Check if the linked list is empty
    def is_empty(self):
        return self.head == None

    # Add a node at the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

     # Add a node at the end
    def add_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node

    # Add a node after a given node
    def add_after(self, key, data):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
            if current == self.head:
                break

    # Add a node before a given node
    def add_before(self, key, data):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.data == key:
            return self.add_at_beginning(data)
        current = self.head
        while current:
            if current.next.data == key:
                new_node = Node(data)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                return

            current = current.next
            if current == self.head:
                break

     # Delete a node
    def delete(self, key):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                print('Hi')
                temp = self.head.prev
                self.head = self.head.next
                self.head.prev = temp
                self.head.prev.next = self.head
            return
        current = self.head
        while current:
            if current.data == key:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:
                break

    # Print the linked list
    def print_list(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # Find a node by value
    def find(self, key):
        if self.is_empty():
            print("List is empty")
            return None
        current = self.head
        while True:
            if current.data == key:
                return current
            current = current.next
            if current == self.head:
                break
        print("Key not found")
        return None

     # Reverse the linked list
    def reverse(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        prev = None
        while True:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head.next = prev
        self.head = prev

    # Count the number of nodes
    def count_nodes(self):
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

dll = DoublyCircularLinkedList()
dll.add_at_beginning(12)
dll.add_at_beginning(52)
dll.add_at_beginning(32)
dll.add_at_beginning(67)
dll.print_list()
dll.delete(67)
dll.print_list()


