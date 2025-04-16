'''
File: huffman.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program creates binary
trees to decode a sequence of 1s and 0s
into a Huffman coding. 
'''
class BinaryTree:
    '''
    This class represents a binary tree.
    Its primary method is construct
    It is to be constructed using no parameters.
    The class branches out into various subtrees,
    and the constructed tree's values help
    to form the decoded sequence. 
    '''
    def __init__(self):
        '''
        This is the class constructor. 
        Parameters: none
        returns: nothing
        '''
        self._value = None
        self._left = None
        self._right = None
    
    def build(self, preorder, inorder):
        '''
        This method builds the binary tree.
        Parameters:
        preorder is a list containing the 
        preorder traversal of the tree
        inorder is a list containing the
        inorder traversal of the tree
        Returns: nothing
        '''
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
           
    def __str__(self):
        '''
        This is the string method of the class.
        Parameters: none
        Returns: a string representation of
        the binary tree object.
        '''
        if self._value == None:
            return "None"
        else:
            return "({} {} {})".format(self._value,str(self._left),\
            str(self._right))

def postorder(tree):
    '''
    This function prints out the postorder
    traversal of the tree.
    Parameters: tree is a BinaryTree.
    Returns: nothing
    '''
    if tree == None:
        return
    else:
        # Recurse to get the bottom nodes.
        postorder(tree._left)
        postorder(tree._right)
        if tree._value != None:
            print(str(tree._value) + " ", end = "")


def decode(tree, sequence):
    '''
    This function takes a string of 1s and 0s
    and uses the constructed tree to decode
    the sequence.
    Parameters:
    tree is a BinaryTree
    sequence is a string of 1s and 0s representing
    a sequence to be decoded using the values of tree.
    '''
    sequenced_list = []
    value = tree._value
    if value == None:
        return
    else:
        # Duplicate the tree
        new_tree = tree
        # Account for the tree being only one node
        if tree._left == None and tree._right == None:
            return tree._value
        # Iterate through the sequence
        for i in sequence:
            if i == '0':
                new_tree = new_tree._left
                # Check if the tree is empty
                if new_tree._value == None:
                    return
                # Reset the tree if necessary
                if new_tree._left == None and\
                      new_tree._right == None:
                    sequenced_list.append(new_tree._value)
                    new_tree = tree
            if i == '1':
                new_tree = new_tree._right
                # Check if the tree is empty
                if new_tree._value == None:
                    return
                # Reset the tree if necessary
                if new_tree._left == None and\
                      new_tree._right == None:
                    sequenced_list.append(new_tree._value)
                    new_tree = tree
        return "".join(sequenced_list)

def main():
    '''
    This is the main method, which creates the
    BinaryTree object to be used in decoding. 
    '''
    file_name = input("Input file: ")
    file = open(file_name, 'r')
    # Get the traversals and sequence
    line_number = 1
    inorder = []
    preorder = []
    sequence = ""
    for line in file:
        if line_number == 1:
            preorder = line.split()
        elif line_number == 2:
            inorder = line.split()
        else:
            sequence = line
        line_number += 1
    file.close()
    tree = BinaryTree()
    tree.build(preorder, inorder)
    postorder(tree)
    print("\n")
    if decode(tree, sequence) != None:
        print(decode(tree,sequence))
    

main()