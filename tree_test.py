class BinaryTree:
    def __init__(self):
        self._value = None
        self._left = None
        self._right = None
    
    def preorder(self):
        if self == None:
            return []
        else:
            return [self._value] + self._left.preorder() \
            + self._right.preorder()
    
    def inorder(self):
        if self._value == None:
            return []
        else:
            self._left.inorder() + [self._value]\
            + self._right.inorder()
    
    def postorder(self):
        if self._value == None:
            return []
        else:
            self._left.postorder() + self._right.postorder()\
            + [self._value]

    def build(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return
        elif len(preorder) == 1 or len(inorder) == 1:
            self._value = preorder[0]
            return

        self._value = preorder[0]
        self._left = BinaryTree()
        self._right = BinaryTree()
        item = preorder[0]
        index = inorder.index(item)
        # Slice the list into left and right subtrees
        self._left.build(preorder[1:index + 1], inorder[0:index])
        self._right.build(preorder[index + 1:], inorder[index + 1:])

def main():
    preorder = [3,4,6,1,7,8,2]
    inorder = [6,4,7,1,8,3,2]
    tree = BinaryTree()
    tree.build(preorder, inorder)
    print(tree.preorder())
    print(tree.inorder())
    print(tree.postorder())

main() 
