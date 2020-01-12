import unittest
from tree import Node, BinarySearchTree



# Write a function that determines whether a given binary tree is a binary search tree.
def check_bst(t):
    node = t.root
    if not node:
        return False
    
    return _check_bst(node, -9999999, 9999999)


def _check_bst(node, min_range, max_range):
    if not node:
        return True

    value = node.item
    left, right = node.left, node.right

    if left and not _check_bst(left, min_range, value) or right and not _check_bst(right, value, max_range):
        return False

    if min_range < value <= max_range:
        return True
    return False


class Test(unittest.TestCase):
    
    def test(self):
        # Using the BST class, but it is not always a BST.
        t = BinarySearchTree()
        t.insert(0)
        self.assertEqual(check_bst(t), True)
        r = t.root
        r.left = Node(1)
        self.assertEqual(check_bst(t), False)
        r.left = Node(0)
        self.assertEqual(check_bst(t), True)
        r.right = Node(0)
        self.assertEqual(check_bst(t), False)
        r.left = Node(-1)
        r.right = Node(2)
        self.assertEqual(check_bst(t), True)
        r.left.left = Node(-3)
        r.left.right = Node(-2)
        self.assertEqual(check_bst(t), False)
        r.left.right = Node(3)
        self.assertEqual(check_bst(t), False)
        r.left.right = Node(-0.5)
        self.assertEqual(check_bst(t), True)
        r.right.left = Node(-10)
        self.assertEqual(check_bst(t), False)
        r.right.left = Node(1.5)
        self.assertEqual(check_bst(t), True)
        r.right.right = Node(2)
        self.assertEqual(check_bst(t), False)
        r.right.right = Node(4)
        self.assertEqual(check_bst(t), True)
        r.right.left = Node(2)
        self.assertEqual(check_bst(t), True)
        r.right.left = Node(3)
        self.assertEqual(check_bst(t), False)
        

if __name__ == '__main__':
    unittest.main()
