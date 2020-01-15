import unittest
from tree import Node, BinarySearchTree



# There are two big binary trees T1 and T2.
# Assuming T1 is much bigger than T2, check whether T2 is a subtree of T1.
# If the subtree of a node N in T1 is the same as T2, T2 is a subtree of T1.
def check_subtree(node, t2):
    if t2 is None:
        return True
        
    if node is None:
        return False

    if preorder_traversal(node) == preorder_traversal(t2.root):
        return True
    
    is_left_same = check_subtree(node.left, t2)
    is_right_same = check_subtree(node.right, t2)
    return is_left_same or is_right_same


def preorder_traversal(root):
    # Add Nonetype to the list in order to save the structure of the tree.
    if root is None:
        return [None]

    return [root.item] + preorder_traversal(root.left) + preorder_traversal(root.right)


# This function does not traverse until the node is the same as T2.root.
def check_subtree_advanced(node, t2):
    if t2 is None:
        return True
    
    if node is None:
        return False

    if node is t2.root:
        if preorder_traversal(node) == preorder_traversal(t2.root):
            return True
    
    return check_subtree_advanced(node.left, t2) or check_subtree_advanced(node.right, t2)


class Test(unittest.TestCase):

    def test(self):
        t1, t2 = BinarySearchTree(), BinarySearchTree()
        t1.insert(0)
        r = t1.root
        r.left = Node(1)
        r.right = Node(3)
        r.left.left = Node(4)
        r.left.right = Node(5)
        r.right.left = Node(6)
        r.right.right = Node(7)
        t2.insert(5)
        t2.insert(6)
        t2.insert(4)
        t2.insert(7)
        t2.insert(8)
        self.assertEqual(check_subtree(t1.root, t2), False)
        self.assertEqual(check_subtree_advanced(t1.root, t2), False)
        r.left.left.right = t2.root
        # Now t2 is a subtree of t1.
        self.assertEqual(check_subtree(t1.root, t2), True)
        self.assertEqual(check_subtree_advanced(t1.root, t2), True)
        self.assertEqual(check_subtree(t1.root.left.left, t2), True)
        self.assertEqual(check_subtree_advanced(t1.root.left.left, t2), True)
        r.left.left.right = Node(10)
        r.right.left.right = t2.root
        self.assertEqual(check_subtree(t1.root, t2), True)
        self.assertEqual(check_subtree_advanced(t1.root, t2), True)


if __name__ == "__main__":
    unittest.main()
