#python program to demonstrate Circular Linked List
#Author Vishvajit Bakrola

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data, self.head)
        current = self.head
        new_node.next_node = self.head

        if self.head is not None:
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
        else:
            new_node.next_node = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            new_node.next_node = new_node
            self.head = new_node
        else:
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
            new_node.next_node = self.head

    def delete_by_value(self, data):
        current = self.head
        prev = None
        while current.next_node != self.head:
            if current.data == data:
                if prev is not None:
                    prev.next_node = current.next_node
                else:
                    while current.next_node != self.head:
                        current = current.next_node
                    current.next_node = self.head.next_node
                    self.head = self.head.next_node
                return
            prev = current
            current = current.next_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next_node
            if current == self.head:
                break

# Example usage:

circular_linked_list = CircularLinkedList()
circular_linked_list.insert_at_start(1)
circular_linked_list.insert_at_end(2)
circular_linked_list.insert_at_end(3)
circular_linked_list.insert_at_end(4)
circular_linked_list.print_list()
# Output: 1 2 3 4
circular_linked_list.delete_by_value(3)
circular_linked_list.print_list()
# Output: 1 2 4
