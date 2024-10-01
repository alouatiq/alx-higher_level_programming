#!/usr/bin/python3
"""
This module defines a class for a singly linked
list node and a class to manage the list.
"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new node for the singly linked list.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the list (default is None).
        """
        self.data = data  # Uses the setter for validation
        self.next_node = next_node  # Uses the setter for validation

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node with validation."""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list in increasing order of the data.

        Args:
            value (int): The data for the new node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Find the correct position to insert
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the singly linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
