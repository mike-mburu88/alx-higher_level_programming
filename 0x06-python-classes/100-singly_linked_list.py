#!/usr/bin/python3
""" first define classes for a singly-linked list."""
class Node:
    """Have a node represented in a list"""
    def __init__(self, data, next_node=None):
        """represent the arguments for the node"""
        self.data = data
        self.next_node = next_node
        
    def data(self):
         """method to get and set the Node Data"""
         return (self.__data)
    def data(self, value):
       if not isinstance(value, int):
           raise TypeError("data must be an integer")
       self.__data = value
    def next_node(self):
       """setting the following node data"""
        return (self.__next_node)
    def next_node(self, value):
         if not isinstance(value, Node) and value is not None:
             raise TypeError("next_node must be a Node object")
         self.__next_node = value
class SinglyLinkedList:
    """define the class for a linked list"""
     def __init__(self):
         """initialize the singly linked list arguments"""
          self.__head = None
     def sorted_insert(self, value):
         """Insert a new node based on the numerical position"""
          new = Node(value)
          if self.__head is None:
              new.next_node = None
               self.__head = new
          elif self.__head.data > value:
              new.next_node = self.__head
              self.__head = new
          else:
              tmp = self.__head
              while (tmp.next_node is not None and tmp.next_node.data < value):
                  tmp = tmp.next_node
                  new.next_node = tmp.next_node
                  tmp.next_node = new
            

            
    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
    
