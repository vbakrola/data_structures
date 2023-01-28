# Data Structures

## Linked Data Structures

1.	Linked List Experiment: Implement and test a singly linked list, doubly linked list, circular linked list, and circular doubly linked list.

### Singly Linked List
A singly linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. It is a data structure in which each node contains a data element and a reference (link) to the next node in the sequence.

The first node of a singly linked list is called the head, and the last node is called the tail. In some cases, the head and the tail are not explicitly distinguished, but rather the list is considered circular and the last node points back to the first node. Singly linked lists are often used to implement other data structures, such as stacks and queues. They are also used to implement dynamic memory allocation, as each node can be dynamically allocated, and the pointers are used to create the links between the nodes.

A singly linked list has the advantage of being a dynamic data structure, as it can grow or shrink during the execution of a program. It also requires less memory than doubly linked list because it only contains one reference (link) per node.
[Python code for Singly Linked List](https://github.com/vbakrola/data_structures/blob/main/Singly%20Linked%20List.py)

### Doubly Linked List
A doubly linked list is a data structure in which each node contains a data element and two references or links, one to the previous node and one to the next node in the sequence. It is a variation of the singly linked list, where each node has two pointers instead of one. The first node of a doubly linked list is called the head, and the last node is called the tail. In some cases, the head and the tail are not explicitly distinguished, but rather the list is considered circular and the last node points back to the first node.

Doubly linked lists are used to implement other data structures, such as stacks and queues, and are also used to implement dynamic memory allocation. They have the advantage of allowing for traversals in both directions. It also allows for more efficient insertion and deletion operations as it is easy to find both next and previous elements.
[Python code for Doubly Linked List](https://github.com/vbakrola/data_structures/blob/main/Doubly%20Linked%20List.py)

### Circular Linked List
A circular linked list is a variation of the singly or doubly linked list, where the last node points back to the first node, forming a loop. In other words, the next pointer of the last node points to the first node, and the previous pointer of the first node points to the last node. Circular linked lists have some useful properties. For example, they can be used to implement a queue with a fixed-size buffer, where the last element points back to the first element. This way, when the buffer is full, the next insertion will occur at the first element, overwriting it. Also, in circular linked list, there is no need for a sentinel node (dummy node) to indicate the end of the list.
[Python code for Circular Linked List](https://github.com/vbakrola/data_structures/blob/main/Circular%20Linked%20List.py)

### Circular Doubly Linked List
A circular doubly linked list is a variation of the doubly linked list data structure, in which the last node's next pointer points to the first node, and the first node's previous pointer points to the last node. This creates a circular loop, so traversing the list in either direction will not reach a null or None reference.

A doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes. In a circular doubly linked list, the head node's previous link points to the tail node and the tail node's next link points to the head node. This type of data structure is useful when we want to traverse the list in both directions (forward and backward) efficiently, and also when we want to quickly insert or remove a node from the list.
[Python code for Circular Doubly Linked List](https://github.com/vbakrola/data_structures/blob/main/Circular%20Doubly%20Linked%20List.py)

## Summary
In summary, Singly linked list only allows traversing in one direction, doubly linked list allows traversing in both directions and circular linked list is a variation of singly or doubly linked list, where last node points back to the first node forming a loop. And circular doubly linked list is a variation of doubly linked list, where the last node points to the first node and the first node points to the last node, forming a loop in both directions.
