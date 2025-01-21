class Node:
    def __init__(self, Data):
        self.data = Data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Add a node at the end of the circular linked list.
        """
        new_node = Node(data)
        if not self.head:
            # If the list is empty, point the head to the new node and form a circle
            self.head = new_node
            new_node.next = self.head
        else:
            # Traverse to the last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node  # Link the last node to the new node
            new_node.next = self.head  # Form the circular link

    def prepend(self, data):
        """
        Add a node at the beginning of the circular linked list.
        """
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            # If the list is empty, form a circular link
            self.head = new_node
            new_node.next = self.head
        else:
            # Traverse to the last node
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node  # Link the last node to the new head
            self.head = new_node  # Update the head pointer

    def delete(self, key):
        """
        Delete a node with the given key from the circular linked list.
        """
        if not self.head:
            print("The list is empty. Nothing to delete.")
            return

        current = self.head
        prev = None

        # Case 1: The head node is the node to be deleted
        if current.data == key:
            if current.next == self.head:
                # If the list contains only one node
                self.head = None
            else:
                # Update the links to skip the head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  # Point the last node to the new head
                self.head = self.head.next  # Update the head pointer
            return

        # Case 2: The node to be deleted is not the head
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:
                prev.next = current.next  # Update the link to skip the current node
                print("Deleted from the list.")
                return
            prev = current
            current = current.next

    def display(self):
        """
        Display all the elements of the circular linked list.
        """
        if not self.head:
            print("The list is empty.")
            return

        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return nodes

    def search(self, key):
        """
        Search for a node with the given key in the circular linked list.
        """
        if not self.head:
            print("The list is empty.")
            return False

        current = self.head
        while True:
            if current.data == key:
                print("Found in the list.")
                return True
            current = current.next
            if current == self.head:
                break

        print("not found in the list.")
        return False

    def length(self):
        """
        Count the number of nodes in the circular linked list.
        """
        if not self.head:
            return 0

        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break

        return count

cll = CircularLinkedList()
cll.append(12)
cll.append(52)
cll.append(72)
cll.prepend(34)
cll.delete(52)
cll.search(52)
print(cll.display())
print(cll.length())