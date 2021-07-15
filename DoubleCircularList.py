# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:52:36 2021

@author: Enrique Velasco
"""

class Double_Circular_List:
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
        
        array = []
        current_node = self.head
        start = True
        counter = self.size
        
        while counter != 0:
            if start != False or current_node != self.head:
                array.append(current_node.value)
                current_node = current_node.next_node
                start = False
                counter -= 1
            else:
                break
        
        return str(array) + " Size: " + str(self.size)
    
    #Insert in the first position
    def prepend(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            new_node.previous_node = self.tail
            self.head.previous_node = new_node
            self.tail.next_node = new_node
            self.head = new_node
        
        self.size += 1
    
    #Insert in the last position
    def append(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            new_node.previous_node = self.tail
            self.head.previous_node = new_node
            self.tail.next_node = new_node
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
            new_head.previous_node = self.tail
            self.tail.next_node = new_head
            node_deleted.next_node = None
            node_deleted.previous_node = None
            self.head = new_head
            
            self.size -= 1
        
    #Delete the last node
    def pop(self):
        
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            node_deleted = self.tail
            new_tail = node_deleted.previous_node
            new_tail.next_node = self.head
            self.head.previous_node = new_tail
            node_deleted.next_node = None
            node_deleted.previous_node = None
            self.tail = new_tail
            
            self.size -= 1
    
    #GET
    def get(self, index):
        
        if index == 0:
            print(self.head.value)
            return self.head
        elif index == self.size - 1:
            print(self.tail.value)
            return self.tail
        elif not ( index >= self.size or index < 0 ):
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
        
        if not( index > self.size - 1 or index < 0):
            node_to_update = self.get(index)
            node_to_update.value = value
        else:
            return None
            
    
    #Insert
    def insert(self, index, value):
        
        if index == 0:
            self.prepend(value)
        elif index == self.size - 1:
            self.append(value)
        elif not ( index >= self.size or index < 0 ):
            new_node = self._Node(value)
            current_node = self.get(index)
            previous_nodes = current_node.previous_node
            new_node.next_node = current_node
            new_node.previous_node = previous_nodes
            previous_nodes.next_node = new_node
            current_node.previous_node = new_node
            
            self.size += 1
            
        else:
            return None
    
    #Remove
    def remove(self, index):
        
        if index == 0:
            self.shift()
        elif index == self.size - 1:
            self.pop()
        elif not ( index >= self.size or index < 0 ):
            node_to_delete = self.get(index)
            previous_nodes = node_to_delete.previous_node
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
        self.head.previous_node = None
        self.tail.next_node = None
        current_node = self.head
        self.tail = current_node
        
        while current_node != None:
            reverse_nodes = current_node.previous_node
            current_node.previous_node = current_node.next_node
            current_node.next_node = reverse_nodes
            current_node = current_node.previous_node
        
        self.head = reverse_nodes.previous_node
        self.head.previous_node = self.tail
        self.tail.next_node = self.head
    

dcl = Double_Circular_List()

dcl.append('A')
dcl.append('B')
dcl.append('C')
dcl.append('D')
print(dcl)

dcl.prepend('AA')
dcl.prepend('BB')
dcl.prepend('CC')
dcl.prepend('DD')
print(dcl)


dcl.pop()
print(dcl)

dcl.shift()
print(dcl)

dcl.get(3)

dcl.update(3, 'ddf')
print(dcl)

dcl.insert(4, 'jdhd')
print(dcl)

dcl.remove(6)
print(dcl)

dcl.reverse()
print(dcl)

