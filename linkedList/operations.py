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
        if current and current.data == key:
            self.head = current.next
            current = None
            return

ll = LinkedList()
ll.insert_after()