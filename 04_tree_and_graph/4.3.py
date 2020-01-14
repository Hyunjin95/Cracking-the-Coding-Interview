import unittest
from tree import BinarySearchTree
from queue import Queue



# When a binary tree is given, make lists of the nodes at the same depth of the tree.
# If the depth is D, the number of the lists is D.
def lists_of_tree(tree):
    root = tree.root
    lists_of_nodes = [[] for _ in range(tree.get_depth())]
    
    q = Queue()
    q.put((root, 0))
    while not q.empty():
        curr = q.get()
        node, depth = curr[0], curr[1]
        lists_of_nodes[depth].append(node.item)

        if node.left:
            q.put((node.left, depth+1))
        if node.right:
            q.put((node.right, depth+1))
    
    return lists_of_nodes


class Test(unittest.TestCase):
    
    def test(self):
        t = BinarySearchTree()
        t.insert(5)
        self.assertEqual(lists_of_tree(t), [[5]])
        t.insert(3)
        self.assertEqual(lists_of_tree(t), [[5], [3]])
        t.insert(7)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7]])
        t.insert(2)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2]])
        t.insert(4)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4]])
        t.insert(6)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4, 6]])
        t.insert(8)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4, 6, 8]])
        t.insert(9)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4, 6, 8], [9]])
        t.insert(10)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4, 6, 8], [9], [10]])
        t.insert(0)
        self.assertEqual(lists_of_tree(t), [[5], [3, 7], [2, 4, 6, 8], [0, 9], [10]])


if __name__ == '__main__':
    unittest.main()
