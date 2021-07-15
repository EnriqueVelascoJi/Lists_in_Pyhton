# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:12:33 2021

@author: Enrique Velasco
"""

class Double_Linked_List:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
            self.previous_node = None
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        
        #Show all items from the list
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
            
        return str(array) + 'Size: ' + str(self.size)
    
    #Insert in the first position
    def prepend(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node 
            self.tail  = new_node
        else:
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
        
        self.size += 1
    
    #Insert in the last position
    def append(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
        
        self.size += 1
    
    #Delete the first node
    def shift(self):
        
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            node_deleted = self.head
            new_head = node_deleted.next_node
            node_deleted.next_node = None
            new_head.previous_node = None
            self.head = new_head
            
            self.size -= 1
            
            return print(node_deleted.value)
    
    #Delete the last node
    def pop(self):
        
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            node_deleted = self.tail
            new_tail = node_deleted.previous_node
            new_tail.next_node = None
            node_deleted.previous_node = None
            self.tail = new_tail
            
            self.size -= 1
            return print(node_deleted.value)
    
    #Get
    def get(self, index):
        
        if index == 0:
            print(self.head.value)
            return self.head
        elif index == self.size - 1:
            print(self.tail.value)
            return self.tail
        elif not( index >= self.size or index < 0):
            counter = 0
            current_node = self.head
            while counter != index:
                current_node = current_node.next_node
                counter += 1
            print(current_node.value)
            return current_node
        else:
            return None
    
    #Update
    def update(self, index, value):
        
        node_to_update = self.get(index)
        
        if node_to_update != None:
            node_to_update.value = value
        else:
            return None
    
    #Insert a node anywhere
    def insert(self, index, value):
        
        if index == 0:
            self.prepend(value)
        elif index == self.size - 1:
            self.append(value)
        elif not( index >= self.size or index < 0):
            new_node = self._Node(value)
            previous_nodes = self.get(index - 1)
            next_nodes = previous_nodes.next_node
            new_node.next_node = next_nodes
            previous_nodes.next_node = new_node
            next_nodes.previous_node = new_node
            new_node.previous_node = previous_nodes
            
            self.size += 1
            
        else:
            return None
    
    #Delete a ndoe anywhere
    def remove(self, index):
        
        if index == 0:
            self.shift()
        elif index == self.size - 1:
            self.pop()
        elif not( index >= self.size or index < 0 ):
            node_to_delete = self.get(index)
            previous_nodes= node_to_delete.previous_node
            next_nodes = node_to_delete.next_node
            previous_nodes.next_node = next_nodes
            next_nodes.previous_node = previous_nodes
            node_to_delete.next_node = None
            node_to_delete.previous_node = None
            
            self.size -= 1
            
        else:
            return None
            
    #Reverse
    def reverse(self):
        
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        
        while current_node != None:
            reverse_nodes = current_node.previous_node
            current_node.previous_node = current_node.next_node
            current_node.next_node = reverse_nodes
            current_node = current_node.previous_node
        self.head = reverse_nodes.previous_node
    
dll = Double_Linked_List()

dll.append('a')
dll.append('b')
dll.append('c')
dll.append('d')
print(dll)  

dll.prepend('0')
dll.prepend('1')
print(dll)

dll.get(3)
print(dll)

dll.insert(2, 'jhhh')
print(dll)

dll.remove(5)
print(dll)

dll.reverse()
print(dll)

"""
dll.update(10, 'bb')
print(dll)
dll.pop()
print(dll)

dll.shift()
print(dll)
"""