#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HOMEWORK 3

Created on Mon Jan 27 17:02:53 2020

@author: hunterharralson
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # initialize pointer to null
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self,data):
        node = Node(data)
        self.first = node
        self.last = node
        self.n = 1 # number of elements in the linked list
        self.curr_node = node # for iteration
        
    def append(self,new_data):
        # adds new data to a new node at the end of the list
        new_node = Node(new_data)
        self.last.next = new_node # update next field of the node
        self.last = new_node
        self.n += 1
    
    '''
    comment out  __iter__ and __next__ methods out to see the generator operate
    '''
    # allows the list to be iterated with a for loop
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.curr_node is None:
            self.curr_node = self.first # so that 2 for loops can run; resets iterator
            raise StopIteration
        else: 
            data = self.curr_node.data
            self.curr_node = self.curr_node.next
            return data
    
    def __len__(self):
        return self.n
    
    def __str__(self,):
        str1 = '['
        for i in self:
            str1 = str1 + str(i) + '->'
        str1 = str1 + ']'
        return str1
        
    def __repr__(self):
        str1 = '['
        for i in self:
            str1 = str1 + repr(i) + '->'
        str1 = str1 + ']'
        return repr(str1)
    
    # overloads the + operator --- coult not figure out the difference b/w the two test cases
    def __add__(self,other):
        self.append(other)
        return self
    
    # overloads the [] operator 
    def __getitem__(self,key):
        ctr = 0
        if key > self.n:
            raise IndexError('list index out of range')
        for i in self:
            if ctr == key:
                return i
            ctr += 1
    
    # allows you to set the value of a node 
    def __setitem__(self,key,value):
        ctr = 1
        if key > self.n:
            raise IndexError('List index out of range')
        for i in self:
            if ctr == key:
                self.curr_node.data = value
            ctr += 1
    
    
    '''
    uncomment out these two methods to see the generator operate
    '''
# =============================================================================
#     # iterator for the generator
#     def __iter__(self):
#         return self.generator()
#     
#     # generator
#     def generator(self):
#         ctr = 0
#         curr_node = self.first
#         while ctr <= self.n:
#            yield curr_node.data
#            curr_node = curr_node.next
# =============================================================================
        
    
    
    
def main():
    a = LinkedList(0)
    a.append(1)
    a.append(2)

    print("7 points if this works")
    for n in a:
        print(n)

    print("")

    print("2 points if this works")
    for n in a:
        print(n)

    print("")

    print("3 points if both of these work")
    for n in a:
        if n == 2:
            break
        else:
            print(n)

    print("")
   
    for n in a:
        if n == 2:
            break
        else:
            print(n)

    print("")

    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    a.append(8)

    print("")

    print("1 points if this works")
    print(len(a))
    print("")

    print("1 points if this works")
    print(str(a))
    print("")
    
    print("1 points if this works")
    print(repr(a))
    print("")


    print("1 points each. That is, 2 points if the output of the next line is correct")
    a[5] = 20
    print(a[5])

    print("")

    print("2 points for correct operation of +")
    a+9 # doesn't modify a
    print(a)

    print("")

    a = a+9 # appends 9 to a
    print(a)


    print("")

    print("1 points for raising correct IndexError")
    try:
        print(a[999])
    except IndexError as e:
        print(e)

    print("")
    
    
if __name__ == '__main__': 
    main()
    
    