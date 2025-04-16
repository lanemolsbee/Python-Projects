class BinarySearchTree:
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None
    
    
    def add(self, value):
        if self._value == None:
            self._value = value
            self._left = BinarySearchTree()
            self._right = BinarySearchTree()
        else:
            if self._value == value:
                return
            else:
                if value < self._value:
                    if self._left._value == None:
                        self._left = BinarySearchTree()
                        self._left._value = value
                        self._left._left = BinarySearchTree()
                        self._left._right = BinarySearchTree()
                    else:
                        self._left.add(value)
                if value > self._value:
                    if self._right._value == None:
                        self._right = BinarySearchTree()
                        self._right._value = value
                        self._right._left = BinarySearchTree()
                        self._right._right = BinarySearchTree()
                    else:
                        self._right.add(value)
                        
    
    def find(self, val):
        if val == self._value:
            return self
        elif self._left and val < self._value:
            return self._left.find(val)
        elif self._right and val > self._value:
            return self._right.find(val)
        else:
            return
            
        
        
    
    def __str__(self):
        if self._value == None:
            return "None"
        else:
            return "({:d} {} {})".format(self._value,str(self._left),\
            str(self._right))



def fmt(spec, values):
    if len(spec) == 0:
        return spec
    if len(values) == 0:
        return spec
    if "{}" not in spec:
        return spec
    else:
        index = find_index(spec, "}", 0)
        replaced = spec[:index - 1] + str(values[0]) +\
            spec[index + 1:]
        return fmt(replaced, values[1:])
    
def find_index(string, elt, index):
    if len(string) == 0:
        return None
    else:
        if string[0] == elt:
            return index
        else:
            return find_index(string[1:], elt, index + 1)
        

def shift_tuple(tup, value):
    first_elts = list(tup[1:len(tup)])
    first_elts.append(value)
    return tuple(first_elts)