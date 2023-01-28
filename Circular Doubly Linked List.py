#python program to demonstrate Circular Linked List
#Author Vishvajit Bakrola

class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next_node = self.head
        if self.head:
            while current.next_node != self.head:
                current = current.next_node
            current.next_node = new_node
            self.head.prev_node = new_node
            new_node.prev_node = current
        else:
            new_node.next_node = new_node
            new_node.prev_node = new_node
        self.head = new_node

    def delete_by_value(self, data):
        current = self.head
        if current is not None:
            if current.data == data:
                if current.next_node == current:
                    current = None
                    return
                else:
                    while current.next_node != self.head:
                        current = current.next_node
                    current.next_node = self.head.next_node
                    self.head.next_node.prev_node = current
                    self.head = self.head.next_node
            else:
                while current.next_node != self.head:
                    if current.next_node.data == data:
                        current.next_node = current.next_node.next_node
                        current.next_node.prev_node = current
                        break
                    current = current.next_node

# create a new circular doubly linked list
cdll = CircularDoublyLinkedList()

# insert some elements
cdll.insert_at_start(3)
cdll.insert_at_start(2)
cdll.insert_at_start(1)

# delete an element
cdll.delete_by_value(2)

