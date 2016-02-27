'''
Created on Jan 30, 2016

@author: grovesr

google foo.bar challenge 4.2

Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid 
laboratory, you had to develop a system to track them, since some habitually 
continue to gnaw on the heads of their brethren and need extra supervision. For
obvious reasons, you based your rabbit survivor tracking system on a binary 
search tree, but all of a sudden that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days) and 
each, luckily enough, had a distinct age. For a given group, the first rabbit 
became the root, and then the next one (taken in order of rescue) was added, 
older ages to the left and younger to the right. The order that the rabbits 
returned to you determined the end pattern of the tree, and herein lies the 
problem.

Some rabbits were rescued from multiple cages in a single rescue operation, 
and you need to make sure that all of the modifications or pathogens 
introduced by Professor Boolean are contained properly. Since the tree did not
preserve the order of rescue, it falls to you to figure out how many different 
sequences of rabbits could have produced an identical tree to your sample 
sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1], it 
would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50 integers 
and returns a string representing the number (in base-10) of sequences that 
would result in the same tree as the given sequence.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
'''

from math import factorial
    
class BinarySearchTree(object):
    '''
    BinarySearchTree object, is a root node pointing to left and right nodes,
    which may be None or BinarySearchTrees themselves
    '''
    _left = None
    _right = None
    _key = None
    
    def __init__(self, key = None, keys = [], left = None, right = None):
        if len(keys) > 0:
            # we are building up a BST from a list of keys
            self._key = keys[0]
        else:
            # we are just creating a root node
            self._key = key
        self._left = left
        self._right = right
        for key in keys[1:]:
            self.insert(newTree = BinarySearchTree(key))
    
    def __repr__(self):
        if self._left is not None:
            left = str(self._left._key)
        else:
            left = str(None)
        if self._right is not None:
            right = str(self._right._key)
        else:
            right = str(None)
        return 'key=%s: left=%s, right=%s' % (str(self._key), left, right)
    
    def insert(self, newTree):
        '''
        Insert a new BinarySearchTree starting at the root node
        '''
        self._insert(self, newTree)
    
    def _insert(self, node = None, newTree = None):
        '''
        Insert a new BinarySearchTree at starting at the given node
        '''
        if node is None:
            node = newTree
            node._left = None
            node._right = None
        if newTree._key < node._key:
            node._right = self._insert(node._right, newTree)
        elif newTree._key > node._key:
            node._left = self._insert(node._left, newTree)
        return node
    
    def get_num_nodes(self):
        '''
        return number of nodes from root down
        '''
        return self._num_nodes(self, 0)
    
    def _num_nodes(self, node = None, nodes = 0):
        '''
        return number of nodes from given node down
        '''
        if node:
            nodes += 1
            nodes = self._num_nodes(node._left, nodes)
            nodes = self._num_nodes(node._right, nodes)
        return nodes
    
    def do_pre_order(self):
        '''
        do pre_order of nodes from root node down
        '''
        self._pre_order(self)
    
    def _pre_order(self, node = None):
        '''
        do pre_order of nodes from given node down
        '''
        if node:
            self._visit(node)
            self._pre_order(node._left)
            self._pre_order(node._right)
    
    def do_in_order(self):
        '''
        do in_order of nodes from root node down
        '''
        self._pre_order(self)
        
    def _in_order(self, node = None):
        '''
        do in_order of nodes from given node down
        '''
        if node:
            self._in_order(node._left)
            self._visit(node)
            self._in_order(node._right)
            
    def do_post_order(self):
        '''
        do post_order of nodes from root node down
        '''
        self._pre_order(self)
    
    def _post_order(self, node = None):
        '''
        do post_order of nodes from given node down
        '''
        if node:
            self._post_order(node._left)
            self._post_order(node._right)
            self._visit(node)
            
    def _visit(self, node):
        '''
        perform some action on the visited node
        '''
        pass
            
    def get_permutations(self):
        '''
        return permutations from root node down
        '''
        return self._permutations(self)
    
    def _permutations(self, node = None):
        '''
        return permutations from given node down
        '''
        if node._left is None and node._right is None:
            # leaf node
            return 1
        leftPermutations = 1
        rightPermutations = 1
        leftNodes = 0
        rightNodes = 0
        if node._left is not None:
            # nodes in left tree
            leftNodes = self._num_nodes(node._left)
            # permutations possible in left tree
            leftPermutations = self._permutations(node._left)
        if node._right is not None:
            # nodes in right tree
            rightNodes = self._num_nodes(node._right)
            # permutations possible in left tree
            rightPermutations = self._permutations(node._right)
        totalNodes = leftNodes + rightNodes
        minNodes = min(leftNodes, rightNodes)
        # combinations of nodes in left and right trees
        combinations = (factorial(totalNodes) / factorial(minNodes)) / factorial(totalNodes - minNodes)
        # total possible permutations from root down
        return leftPermutations * rightPermutations * combinations
    
def answer(seq):
    # create a BinarySearchTree based on the given sequence
    bTree = BinarySearchTree(keys = seq)
    bTree.get_num_nodes()
    # calculate the number of input permutations that will result in the 
    # same BinarySearchTree
    permutations = bTree.get_permutations()
    return str(permutations)

if __name__ == '__main__':
    seq = [5, 9, 8, 2, 1]
    print answer(seq)
    seq = [5, 2, 9, 8, 1]
    print answer(seq)
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print answer(seq)
    seq = [4, 2, 1, 3, 5, 6]
    print answer(seq)
    seq = [3, 2, 1, 4]
    print answer(seq)
    seq = [4, 3, 2, 1]
    print answer(seq)
    seq = [1, 3, 2, 4]
    print answer(seq)
#     cProfile.run('answer(seq)')