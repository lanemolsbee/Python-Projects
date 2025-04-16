class LinkedList:
    def __init__(self):
        self._head = None
    
    # sort the nodes in the list
    def sort(self):
        '''
        This function sorts the LinkedList object
        in descendingg order. 
        Parameters: None
        Returns: the sorted LinkedList
        '''
        sorted = LinkedList()
        if self._head == None:
            return None
        
        
         
        while self._head != None:            
            # Removes a node to be placed
            curr_element = self.remove()        
            
            if sorted._head == None:
                sorted._head = curr_element
            # Add a node to the head if the new node is greater
            elif sorted._head.value() < curr_element.value():
                sorted.add(curr_element)
            else:
                # Find the first node less than curr_element
                E1 = sorted._head
                while E1 != None:
                    if E1.value() < curr_element.value():
                        break
                    E1 = E1._next
                # Determine where to place the node
                E = sorted._head
                while E._next is not E1:
                    E = E._next
                
                sorted.insert(E, curr_element)
            
        self._head = sorted._head
        return self._head


    # add a node to the head of the list
    def add(self, node):
        node._next = self._head
        self._head = node
        
    # remove a node from the head of the list and return the node
    def remove(self):
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node
    
    # insert node2 after node1
    def insert(self, node1, node2):
        assert node1 != None
        node2._next = node1._next
        node1._next = node2
    
    def __str__(self):
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def __str__(self):
        return str(self._value) + "; "
    
    def value(self):
        return self._value
    
    def next(self):
        return self._next

def main():
    '''
    This is the main function, which tests the 
    sort function. 
    Parameters: None
    Returns: nothing
    '''
    file_name = input()
    file = open(file_name, 'r')
    numbers = []
    to_be_sorted = LinkedList()
    for line in file:
        numbers = line.split()
    for n in numbers:
        # Cast the value to an integer
        node = Node(int(n))
        to_be_sorted.add(node)
    to_be_sorted.sort()
    print(to_be_sorted)

main()    


