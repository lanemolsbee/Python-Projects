def str2objects(spec):
    elts = spec.split(None, 1)
    if len(elts) == 0:
        return []
    
    if len(elts) == 1:
        if elts[0] == "dict":
            return [{}]
        elif elts[0] == "list":
            return [[]]
        elif elts[0] == "str":
            return ['']

def preorder_to_bst(preorder):
    if len(preorder) == 0:
        return None
    elif len(preorder) == 1:
        return BinarySearchTree(preorder[0])
    else:
        tree = BinarySearchTree(preorder[0])
        less_than = []
        greater_than = []
        for i in range(1,len(preorder)):
            if preorder[i] < preorder[0]:
                less_than.append(preorder[i])
            elif preorder[i] > preorder[0]:
                greater_than.append(preorder[i])
        tree._left = preorder_to_bst(less_than)
        tree._right = preorder_to_bst(greater_than)
        return tree

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        
    # your code goes here
    def remove_last(self):
        curr = self._head
        if curr == None:
            return None
        if curr._next == None:
            self._head = None
            self._tail = None
            return curr
        while curr._next._next != None:
            curr = curr._next
        node = curr._next
        curr._next = None
        self._tail = curr
        return node

    def add(self,new):
        new._next = self._head
        # if the list is empty, both
        # the head and tail will reference
        # this new node
        if self._head == None:
            self._tail = new 
        self._head = new 


    def __str__(self):
        string = 'LList -> '
        current = self._head
        while current != None:
            string += str(current)
            current = current._next
        return string + '; tail -> ' + str(self._tail)
        
class Node:
    def __init__(self,value):
        self._value = value
        self._next = None

    def __str__(self):
        if self._next == None:
            nxt = "None"
        else:
            nxt = "->"
        return " |" + str(self._value) + "|:" + nxt

class Queue:
    def __init__(self):
        self._items = ""

    def enqueue(self, item):
        if len(self._items) == 0:
            self._items += item
        else:
            self._items += "," + item

    def dequeue(self):
        removed = self._items[0]
        self._items = self._items[2:]
        return removed

    def is_empty(self):
        if len(self._items) == 0:
            return True
        return False

    def __str__(self):
        return self._items.replace(",","")