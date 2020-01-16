import unittest
import random
from tree import Node



# We want to implement a binary tree class from scratch.
# It includes insert() and search() of a node and a getRandomNode() method which returns arbitrary node.
# getRandomNode() returns any node from all nodes in the tree with the same probability. 
class NodeWithSize(Node):
    """ A Node class with a size of itself and its children. Inherited from the Node class. """
    def __init__(self, item):
        super().__init__(item)
        self._size = 1
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
    

class BinaryTree:
    """ A binary tree class. """
    def __init__(self):
        self._root = None
    
    def __str__(self):
        str_list = [str(x) for x in self._inorder_traversal(self._root)]
        return " -> ".join(str_list)

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, root):
        self._root = root
    
    def get_size(self):
        return self._root.size if not self.is_empty() else 0
    
    def insert(self, item):
        n = self._insert_helper(self.root, item)
        if self.is_empty():
            self.root = n
        return n
            
    def _insert_helper(self, node, item):
        if node is None:
            return NodeWithSize(item)
        
        if item <= node.item:
            node.left = self._insert_helper(node.left, item)
        else:
            node.right = self._insert_helper(node.right, item)

        node.size += 1
        return node
    
    def search(self, item):
        return self._search_helper(self.root, item)
    
    def _search_helper(self, node, item):
        if node is None or node.item == item:
            return node
        if item <= node.item:
            return self._search_helper(node.left, item)
        if item > node.item:
            return self._search_helper(node.right, item)

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def get_random_node(self):
        return self._get_random_node_helper(self.root) if not self.is_empty() else None
    
    def _get_random_node_helper(self, node):
        left_size = node.left.size if node.left is not None else 0
        random_num = random.randint(0, node.size-1)

        if random_num < left_size:
            return self._get_random_node_helper(node.left)
        elif random_num == left_size:
            return node
        else:
            return self._get_random_node_helper(node.right)

    def _inorder_traversal(self, root):
        if root is None:
            return []
        return self._inorder_traversal(root.left) + [root.item] + self._inorder_traversal(root.right)


class EfficientBinaryTree(BinaryTree):
    """ A binary tree class that implements get_random_node() more efficiently """
    def get_random_node(self):
        if self.is_empty():
            return None
        
        # This number will be reused over the recursion.
        random_num = random.randint(0, self.root.size-1)
        return self._get_random_node_helper(self.root, random_num)
    
    def _get_random_node_helper(self, node, i):
        left_size = left_size = node.left.size if node.left is not None else 0
        
        if i < left_size:
            return self._get_random_node_helper(node.left, i)
        elif i == left_size:
            return node
        else:
            return self._get_random_node_helper(node.right, i - (left_size+1))


class Test(unittest.TestCase):
    
    def test(self):
        t = BinaryTree()
        self.assertEqual(t.get_size(), 0)
        self.assertEqual(t.is_empty(), True)
        self.assertEqual(t.get_random_node(), None)
        t.insert(3)
        self.assertEqual(t.get_random_node(), t.root)
        t.insert(1)
        t.insert(5)
        t.insert(0)
        self.assertEqual(t.get_size(), 4)
        self.assertEqual(t.is_empty(), False)
        self.assertEqual(t._inorder_traversal(t.root), [0, 1, 3, 5])
        self.assertEqual(str(t), "0 -> 1 -> 3 -> 5")
        self.assertEqual(t.root.size, 4)
        self.assertEqual(t.root.left.size, 2)
        self.assertEqual(t.root.left.left.size, 1)
        self.assertEqual(t.root.right.size, 1)
        self.assertEqual(t.search(3), t.root)
        self.assertEqual(t.search(1), t.root.left)
        self.assertEqual(t.search(0), t.root.left.left)
        self.assertEqual(t.search(5), t.root.right)
        self.assertEqual(t.search(4), None)
        nodes = {t.root, t.root.left, t.root.left.left, t.root.right}
        self.assertEqual(t.get_random_node() in nodes, True)

    def test_efficient_ver(self):
        t = EfficientBinaryTree()
        t.insert(3)
        t.insert(1)
        t.insert(5)
        t.insert(0)
        nodes = {t.root, t.root.left, t.root.left.left, t.root.right}
        self.assertEqual(t.get_random_node() in nodes, True)
   

if __name__ == "__main__":
    unittest.main()
