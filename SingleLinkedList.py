# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:25:11 2021

@author: Enrique Velasco
"""

class Single_Linked_list:
    
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
    
    def __init__(self):
        self.head = None
        self.tail =None
        self.size =0
    
    def __str__(self):
        
        #Show all items from the list
        array = []
        current_node = self.head
        while current_node !=  None:
            array.append(current_node.value)
            current_node = current_node.next_node
        
        return str(array) + 'Size: ' + str(self.size)
    
    #Insert in the last position
    def append(self, value):
        
        new_node = self._Node(value)
        
        #In case there is not a node in the list
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            
        self.size +=1
    
    #Insert in the first position
    def prepend(self, value):
        
        new_node = self._Node(value)
        
        #In case there is not a node in the list
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        
        self.size += 1
    
    #Delete the first node
    def shift(self):
        
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            node_deleted = self.head
            self.head = node_deleted.next_node
            node_deleted.next_node = None
            self.size -= 1
            return print(node_deleted.value)
    
    #Delete the last node
    def pop(self):
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            new_tail = current_node
            
            while current_node.next_node !=None:
                new_tail = current_node
                current_node = current_node.next_node
            
            self.tail = new_tail
            self.tail.next_node = None
            self.size -= 1
            return print(current_node.value)
        
    #Get
    def get(self, index):
            
        #Print the tail
        if index == self.size - 1:
            print(self.tail.value)
            return self.tail
        elif index == 0:
            print(self.head.value)
            return self.head
        elif not(index >= self.size or index < 0):
            current_node = self.head
            counter = 0
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
        
        if index == self.size - 1:
            return self.append(value)
        elif not(index >= self.size or index < 0):
            new_node = self._Node(value)
            previous_nodes = self.get(index)
            next_nodes = previous_nodes.next_node
            previous_nodes.next_node = new_node
            new_node.next_node = next_nodes
            self.size += 1
        else:
            return None
        
    #Delete a node anywhere
    def remove(self, index):
        
        if index == self.size - 1:
            self.pop()
        elif index == 0:
            self.shift()
        elif not(index >= self.size or index < 0):
            previous_nodes = self.get(index - 1)
            node_to_remove = self.get(index)
            previous_nodes.next_node = node_to_remove.next_node
            node_to_remove.next_node = None
            return print(node_to_remove.value)
    #Reverse
    def reverse(self):
        
        reverse_node = None
        current_node = self.head
        self.tail = current_node
        while current_node != None:
            next_node = current_node.next_node
            current_node.next_node = reverse_node
            reverse_node = current_node
            current_node = next_node
        self.head = reverse_node  
        return self.head          
        
        
sll = Single_Linked_list()
"""
sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')
"""

sll.prepend('A')
sll.prepend('B')
sll.prepend('C')
sll.prepend('D')
print(sll)
sll.reverse()
print(sll)
