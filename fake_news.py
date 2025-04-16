class Node:
    def __init__(self, word):
        self._word = word
        self._count = 1
        self._next = None
    
    def word(self):
        return self._word
    def count(self):
        return self._count
    def next(self):
        return self._next
    def set_next(self, target):
        self._next = target
    def incr(self):
        self._count += 1
    def __str__(self):
        return "Word:", self._count

class LinkedList:
    def __init__(self):
        self._head = None
    def is_empty(self):
        if self._head == None:
            return True
        return False
    def head(self):
        return self._head
    def update_count(self, word):
        current = self._head
        
        while current._next != None:
            if current.word() == word:
                current.incr()
                return
        current.set_next(word)
    # Reused code from linkedlist_sort
    def rm_from_head(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node(self)
        
    # Used code from linkedlist_sort problem
    def insert_after(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def sort(self):
        sorted = LinkedList()
        if self._head == None:
            return None
                
        while self._head != None:            
            # Removes a node to be placed
            curr_element = self.remove()        
            
            if sorted._head == None:
                sorted._head = curr_element
            # Add a node to the head if the new node is greater
            elif sorted._head.count() < curr_element.count():
                sorted.add(curr_element)
            else:
                # Find the first node less than curr_element
                E1 = sorted._head
                while E1 != None:
                    if E1.count() < curr_element.count():
                        break
                    E1 = E1._next
                # Determine where to place the node
                E = sorted._head
                while E._next is not E1:
                    E = E._next
                
                sorted.insert(E, curr_element)
            
        self._head = sorted._head
        return self._head
    
    def get_nth_highest_count(self, n):
        current = self._head
        while n > 0:
            current = current._next
            n -= 1
        return current._count
    
    def print_upto_count(self, n):
        current = self._head
        while current != None:
            if current._count >= n:
                print(current._count)
    # Used code from linkedlist_sort
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string
    # Used code from linkedlist_sort
    def add(self, node):
        node._next = self._head
        self._head = node

def main():
    import csv
    import string
    file_name = input()
    infilename = file_name
    infile = open(infilename)
    csvreader = csv.reader(infile)

    
main()