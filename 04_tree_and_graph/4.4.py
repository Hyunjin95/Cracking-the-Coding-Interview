import unittest
from tree import BinarySearchTree



# Write a function that checks whether a binary tree given is a balanced tree.
# A balanced tree is that for all nodes, the difference between the heights of the left subtree and the right subtree is at most 1.
def check_balanced_tree(t):
    if not t.root:
        return False

    return get_height_and_balance(t.root) != -1


def get_height_and_balance(n):
    if not n:
        return 0
    
    left_height = get_height_and_balance(n.left)
    right_height = get_height_and_balance(n.right)

    if left_height == -1 or right_height == -1:
        return -1
    
    diff = abs(left_height - right_height)
    if diff > 1:
        return -1
    return max(left_height, right_height) + 1


class Test(unittest.TestCase):

    def test(self):
        t = BinarySearchTree()
        self.assertEqual(check_balanced_tree(t), False)
        t.insert(1)
        self.assertEqual(check_balanced_tree(t), True)
        t.insert(2)
        self.assertEqual(check_balanced_tree(t), True)
        t.insert(0)
        self.assertEqual(check_balanced_tree(t), True)
        t.insert(4)
        t.insert(6)
        self.assertEqual(check_balanced_tree(t), False)
        t.insert(3)
        self.assertEqual(check_balanced_tree(t), False)
        t.insert(-4)
        t.insert(-6)
        self.assertEqual(check_balanced_tree(t), False)
        t.insert(-3)
        t.insert(0.5)
        t.insert(1.5)
        self.assertEqual(check_balanced_tree(t), True)    


if __name__ == '__main__':
    unittest.main()
