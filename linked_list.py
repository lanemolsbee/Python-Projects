'''
File: linked_list.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This file contains code for
specially modified Node and LinkedList
classes with the purpose of finding a 
list of a person's social media friends
and determining the friends in common between
two input people. 
'''
class Node:
    '''
    This is the Node class, which will represent
    a Node in the LinkedList class.
    Its primary methods are add_friend and __str__.
    It is to be constructed using only a string
    object that represents the name of the person. 
    Each Node object contains a sub-linked list that
    represents a person's friends on social media. 
    '''
    def __init__(self, name):
        '''
        This is the constructor method.
        Parameters: name is a string representing
        the name of the person the Node represents.
        Returns: nothing
        '''
        self._name = name
        self._friends = LinkedList()
        self._next = None
    def name(self):
        return self._name
    def friends(self):
        return self._friends
    def add_friend(self, node):
        '''
        This function adds a person to the Node
        object's sublist. 
        Parameters: node is a Node object to
        be added to the sublist self._friends.
        Returns: nothing
        The function makes sure to avoid 
        duplicate friends. It also assumes
        that the person to be added to
        is a Node in the main linked list. 
        '''
        if self._friends._head == None:
            self._friends._head = node
        else:
            current = self._friends._head
            while current != None:
                # Stop if the person is already there. 
                if node.name() == current.name():
                    return
                current = current._next
            node._next = self._friends._head
            self._friends._head = node
    def __str__(self):
        '''
        This function converts the Node to a string.
        Parameters: none
        Returns: the string representation of the object.
        '''
        return self._name + ":" + str(self._friends)
    
    def next(self):
        return self._next
        

class LinkedList:
    '''
    This class represents a sequence of Node
    objects.
    Its primary methods are add_person, add_to_list,
    and friends_in_common, as well as sort.
    It is to be constructed using no parameters. 
    The class does contain several functions that
    exist to help the sort function do its job.
    These functions are otherwise never used. 
    '''
    def __init__(self):
        '''
        This is the class constructor. 
        Parameters: none
        Returns: nothing
        '''
        self._head = None
    
    def head(self):
        return self._head
    def add_person(self, person):
        '''
        This function adds a person the main list.
        Parameters: person is a string representing
        the name of the person to be added. 
        Returns: nothing
        '''
        if self._head == None:
            self._head = Node(person)
        else:
            current = self._head
            while current != None:
                if current.name() == person:
                    return
                current = current._next
            # Add a person if they're not in the list. 
            node = Node(person)
            node._next = self._head
            self._head = node

    def add_to_list(self, a, b):
        '''
        This function adds b to the sublist
        of friends for a. 
        Parameters: a and b are strings
        representing the names of people.
        Returns: nothing
        '''

        if self._head == None:
            self._head = Node(a)
            self._head.add_friend(Node(b))
        else:
            current = self._head
            while current != None:
                # add_friend accounts for duplicates
                if current.name() == a:
                    current.add_friend(Node(b))
                    return
                current = current._next
            # add a person and add person b to their list
            self.add_person(Node(a))
            self._head.add_friend(Node(b))
        
    
    
    def rm_from_head(self):
        '''
        This function removes the head of the linked list.
        Parameters: None
        Returns: nothing
        This code was recycled from another project.
        It also is not used in any other function. 
        It exists solely to help the sort function
        do its work. 
        '''
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node        
    
    def add(self, node):
        '''
        This function adds a node to the head.
        Parameters: node is a Node object
        Returns: Nothing
        This function recycles code from other projects. 
        It is not used in any other function.
        Its puprose is to help the sort function. 
        '''
        node._next = self._head
        self._head = node
    
    def insert_after(self, node1, node2):
        '''
        This function inserts node2 after node 1.
        Parameters: node1 and node2 are Node objects.
        Returns: nothing
        This function recycles code from other projects.
        It is not used in any other function and its
        main purpose is to help the sort function. 
        '''
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def sort(self):
        '''
        This function sorts a Linked List in 
        descending alphabetical order, ie, A-Z.
        Parameters: none
        Returns: the head of the sorted list.
        It sorts the linked list by creating
        a sorted list and removing elements
        from the linked list and adding them
        to the sorted version of the list. 
        '''
        sorted = LinkedList()
        if self._head == None:
            return None
                
        while self._head != None:            
            # Removes a node to be placed
            curr_element = self.rm_from_head()        
            
            if sorted._head == None:
                sorted._head = curr_element
            # Add if the current element count >= the head's count
            elif sorted._head.name() >= curr_element.name():
                sorted.add(curr_element)
            else:
                # Find the first node less than curr_element
                E1 = sorted._head
                while E1 != None:
                    # Account for equal counts.
                    if E1.name() >= curr_element.name():
                        break
                    E1 = E1._next
                # Determine where to place the node
                E = sorted._head
                while E._next is not E1:
                    E = E._next
                
                sorted.insert_after(E, curr_element)
            
        self._head = sorted._head
        return self._head
    
    def friends_in_common(self, person_one, person_two):
        '''
        This function determines the friends in common
        between person_one and person_two. 
        Parameters: person_one and person_two are 
        both strings representing the names of the 
        people to be compared. 
        Returns: a LinkedList that contains as nodes
        the friends in common between
        person_one and person_two. 
        This function performs the main function
        of this program and is critical to its functioning.
        '''
        ones_friends = None
        twos_friends = None
        friends_list = LinkedList()
        current = self._head
        # Get the sublists for the two people
        while current != None:
            if current.name() == person_one:
                ones_friends = current._friends
            elif current.name() == person_two:
                twos_friends = current._friends
            current = current._next
        # Iterate through the first person's list
        current_one = ones_friends._head
        while current_one != None:
            # Compare each person in two's list to each in one's.
            current_two = twos_friends._head
            while current_two != None:
                if current_one.name() == current_two.name():
                    friends_list.add_person(current_one.name())
                current_two = current_two._next
            current_one = current_one._next
        
        return friends_list
    def __str__(self):
        '''
        This function converts the list to a string.
        '''
        if self._head == None:
            return "The list is empty"
        else:
            string_version = '['
            current = self._head
            while current != None:
                string_version += current._name + "; "
                current = current._next
            string_version += "]"
            return string_version
    
    def __contains__(self, person):
        '''
        This function determines whether person
        is in the linked list. 
        Parameters: person is a string
        representing the name of a person
        Returns: a boolean value determining
        whether person is a node in the list. 
        '''
        if self._head == None:
            return False
        current = self._head
        while current != None:
            if current.name() == person:
                return True
            current = current._next
        return False


        
        

        