#python program to demonstrate Doubly Linked List
#Author Vishvajit Bakrola
class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev_node = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data, None, self.tail)
        if self.tail is not None:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def delete_by_value(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev_node is not None:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node
                if current.next_node is not None:
                    current.next_node.prev_node = current.prev_node
                else:
                    self.tail = current.prev_node
                return
            current = current.next_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next_node

# Example usage:

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_at_start(1)
doubly_linked_list.insert_at_end(2)
doubly_linked_list.insert_at_end(3)
doubly_linked_list.insert_at_end(4)
doubly_linked_list.print_list()
# Output: 1 2 3 4
doubly_linked_list.delete_by_value(3)
doubly_linked_list.print_list()
# Output: 1 2 4