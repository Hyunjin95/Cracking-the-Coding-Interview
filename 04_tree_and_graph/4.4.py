import unittest
from tree import BinarySearchTree



# Write a function that checks whether a binary tree given is a balanced tree.
# A balanced tree is that for all nodes, the difference between the heights of the left subtree and the right subtree is at most 1.
def check_balanced_tree(t):
    if t.get_depth() <= 1:
        return True
    
    return check_balance(t.root)

def check_balance(n):
    child = n.left or n.right
    if not child:
        return True
    
    if n.left and n.right:
        left_subtree, right_subtree = BinarySearchTree(n.left), BinarySearchTree(n.right)
        height_left_subtree, height_right_subtree = left_subtree.get_depth(), right_subtree.get_depth()
        if abs(height_left_subtree - height_right_subtree) > 1:
            return False        
        return check_balance(n.left) and check_balance(n.right)
    else:
        subtree = BinarySearchTree(child)
        height = subtree.get_depth()
        if height > 1:
            return False
        return True


def check_height_and_balanced(n, is_balanced):
    if not is_balanced:
        # If one node is not balanced, there is no need to search any other nodes.
        return (-1, False)
    child = n.left or n.right
    if not child:
        return (0, True)

    if n.left and n.right:
        left, right = check_height(n.left), check_height(n.right)
        if not (left[1] or right[1]):
            
    else:
        height = check_height(child)[0] + 1
        return (height, height <= 1 ? is_balanced and True : False)


class Test(unittest.TestCase):

    def test(self):
        t = BinarySearchTree()
        self.assertEqual(check_balanced_tree(t), True)
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
