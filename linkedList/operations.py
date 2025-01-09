class Node:
    def __int__(self, Data):
        self.data = Data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if not current:
            print('Previous node not found')
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head
        # If the node to delete is first node
        if current and current.data == key: # None -> False
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print('Key does not exist')

        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

ll = LinkedList()
ll.insert_after()