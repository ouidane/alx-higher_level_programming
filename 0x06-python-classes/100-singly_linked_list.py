#!/usr/bin/python3
"""
This module defines classes for a singly linked list: Node and SinglyLinkedList.
"""

class Node:
    """
    A class that defines a node of a singly linked list.
    
    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the list.
    """
    
    def __init__(self, data, next_node=None):
        """
        Initializes a Node with the given data and next_node.
        
        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the list (default is None).
        
        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data
    
    @data.setter
    def data(self, value):
        """
        Sets the data of the node with validation.
        
        Args:
            value (int): The data to be set.
        
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node with validation.
        
        Args:
            value (Node or None): The next node to link to this node.
        
        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    
    Attributes:
        __head (Node): The head of the singly linked list.
    """
    
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None
    
    def __str__(self):
        """
        Prints the entire list in a human-readable format, one node number per line.
        
        Returns:
            str: A string representation of the entire list.
        """
        node = self.__head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)
    
    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        
        Args:
            value (int): The data value for the new node.
        
        Raises:
            TypeError: If value is not an integer.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
