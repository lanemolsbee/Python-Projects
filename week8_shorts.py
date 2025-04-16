class BinaryTree:
    def __init__(self,value):
        self._value = value
        self._left = None
        self._right = None

    def value(self):
        return self._value

    def left(self):
        return self._left

    def right(self):
        return self._right

    def insert_right(self, value):
        if self._right == None:
            self._right = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._right = self._right
            self._right = t

    def insert_left(self, value):
        if self._left == None:
            self._left = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t._left = self._left
            self._left = t

def tree_height(tree):
    if tree == None:
        return 0
    if tree.left() == None and tree.right() == None:
        return 0
    else:
        return 1 + max(tree_height(tree.left()), tree_height(tree.right()))

def tree_count(tree):
    if tree == None:
        return 0
    else:
        if tree._left == None and tree._right == None:
            return 1
        return 1 + tree_count(tree.left()) + tree_count(tree.right())
    

def tree_sum(tree):
    if tree == None:
        return 0
    else:
        return tree._value + tree_sum(tree.left()) + tree_sum(tree.right())

def count_interior(tree):
    if tree == None:
        return 0
    else:
        if tree._left == None and tree._right == None:
            return 0
        else:
            return 1 + count_interior(tree.left()) + count_interior(tree.right())