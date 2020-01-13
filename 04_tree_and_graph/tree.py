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


class BinarySearchTree:
    """ A binary search tree
        Attributes:
            node: A root node
    """
    def __init__(self, root=None):
        if root:
            if isinstance(root, Node):
                self._root = root
            else:
                raise RuntimeError("Type expected: Node")
        else:
            self._root = None

    def __str__(self):
        return self.print_inorder(self.root)

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, root):
        self._root = root
    
    def insert(self, item):
        node = Node(item)
        if self.is_empty():
            self.root = node
        else:
            curr = self.root
            while curr:
                if curr.item >= item:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break
    
    def search(self, item):
        node = self.root
        while node:
            if node.item == item:
                return True
            elif node.item < item:
                node = node.right
            else:
                node = node.left
        return False
    
    def print_inorder(self, n):
        if not n:
            return ""
        if not (n.left or n.right):
            return str(n.item)

        return self.print_inorder(n.left) + " -> " + str(n.item) + " -> " + self.print_inorder(n.right)
    
    def is_empty(self):
        if not self.root:
            return True
        return False
    
    def get_depth(self):
        if self.is_empty():
            return 0
        return self._get_depth(self.root)
    
    def _get_depth(self, n):
        if not n:
            return 0
        return max(self._get_depth(n.left), self._get_depth(n.right)) + 1          


class Test(unittest.TestCase):

    def test_bst(self):
        bst = BinarySearchTree()
        bst.insert(3)
        self.assertEqual(bst.get_depth(), 1)
        bst.insert(4)
        self.assertEqual(bst.get_depth(), 2)
        bst.insert(2)
        self.assertEqual(bst.get_depth(), 2)
        bst.insert(0)
        self.assertEqual(bst.get_depth(), 3)
        bst.insert(6)
        self.assertEqual(bst.get_depth(), 3)
        bst.insert(1)
        self.assertEqual(bst.get_depth(), 4)
        print(bst)
        self.assertTrue(bst.search(0))
        self.assertTrue(bst.search(1))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(4))
        self.assertTrue(bst.search(6))
        self.assertFalse(bst.search(5))


if __name__ == '__main__':
    unittest.main()
