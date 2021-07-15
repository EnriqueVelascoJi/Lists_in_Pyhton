# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 20:31:53 2021

@author: Enrique Velasco
"""

class Circular_Linked_List:
    
    class _Node:
        
        def __init__(self, value):
            self.value = value
            self.next_node = None
            
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
        return str(array) + "Size: " + str(self.size)
    
    #Insert in the first position
    def prepend(self, value):
        
        new_node = self._Node(value)
        
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
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
            new_node.next_node= self.head
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
            self.tail.next_node = new_head
            self.head = new_head
            
            self.size -= 1
            
    #Delete the last node
    def pop(self):
        
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            new_tail = self.head
            counter = 0
            while counter != self.size - 1:
                new_tail = new_tail.next_node
                counter += 1
            new_tail.next_node = self.head
            self.tail = new_tail
            
            self.size -= 1
        
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
    def update(self, value, index):
        
        node_to_update = self.get(index)
        
        if node_to_update != None:
            node_to_update.value = value
        else:
            return None
            
    #Insert
    def insert(self, value, index):
        
        if index == 0:
            self.prepend(value)
        elif index == self.size - 1:
            self.append(value)
        elif not ( index >= self.size or index < 0 ):
            new_node = self._Node(value)
            previous_nodes = self.get(index - 1)
            next_nodes = previous_nodes.next_node
            new_node.next_node = next_nodes
            previous_nodes.next_node = new_node
            
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
            previous_nodes = self.get(index - 1)
            node_deleted = previous_nodes.next_node
            next_nodes = self.get(index + 1)
            previous_nodes.next_node = next_nodes
            node_deleted.next_node = None
            
            self.size -= 1
        else:
            return None
    
    #Reverse
    def reverse(self):
        
        reverse_nodes = None
        current_node = self.head
        self.tail = current_node
        start = True
        counter = self.size
        
        while counter != 0:
            if start != False or current_node != self.head:
                next_node = current_node.next_node
                current_node.next_node = reverse_nodes
                reverse_nodes = current_node
                current_node = next_node
                start = False
                counter -= 1
            else:
                break
        
        self.head = reverse_nodes
        self.tail.next_node = self.head
                
        
            
csl = Circular_Linked_List()

csl.prepend('A')
csl.prepend('B')
csl.prepend('C')
csl.prepend('D')

print(csl)

csl.append('E')
csl.append('F')
csl.append('G')
csl.append('H')

print(csl)

csl.pop()
csl.pop()
print(csl)

csl.shift()
print(csl)

csl.get(2)

csl.update('AA', 2)
print(csl)

csl.insert('AAA', 2)
print(csl)

csl.remove(2)
print(csl)

csl.reverse()
print(csl)
