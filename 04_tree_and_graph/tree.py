import unittest



class Node:
    """ A node for trees """
    def __init__(self, item):
        self._item = item
        self._left = None
        self._right = None
    
    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, item):
        self._item = item
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self, left):
        self._left = left
    
    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, right):
        self._right = right


class BinaryTree:
    """ A binary tree """
    def __init__(self):
        self._root = None
    
    def insert(self, item):
        