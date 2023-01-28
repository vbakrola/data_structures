#python program to demonstrate Singly Linked List
#Author Vishvajit Bakrola
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node

    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node is not None:
            if current.next_node.data == data:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node

# Example usage:

linked_list = LinkedList()
linked_list.insert_at_start(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.print_list()
# Output: 1 2 3 4
linked_list.delete_by_value(3)
linked_list.print_list()
# Output: 1 2 4