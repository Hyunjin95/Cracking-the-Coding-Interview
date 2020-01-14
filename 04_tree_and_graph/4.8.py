import unittest
from tree import Node, BinarySearchTree



# When two nodes of a binary tree are given, find the first common ancestor of the nodes.
# Restriction: You cannot save any other node in your data structure. The tree doesn't have to be a BST.
def first_common_ancestor(t, a, b):
    node = t.root
    if not (find(node, a) and find(node, b)):
        return None

    return _first_common_ancestor(node, a, b)
        

def _first_common_ancestor(root, a, b):
    if root is None or root is a or root is b:
        return root

    a_is_left, b_is_left = find(root.left, a), find(root.left, b)
    if a_is_left != b_is_left:
        return root
    
    child = root.left if a_is_left else root.right
    return _first_common_ancestor(child, a, b)


def find(root, dest):
    if root is None:
        return False
    if root is dest:
        return True
    
    return find(root.left, dest) or find(root.right, dest)


class Test(unittest.TestCase):

    def test(self):
        t = BinarySearchTree()
        t.insert(1)
        root = t.root
        root.left = Node(2)
        root.right = Node(3)
        self.assertEqual(first_common_ancestor(t, root.left, root.right), root)
        self.assertIsNone(first_common_ancestor(t, root.left, Node(4)), None)
        root.left.left = Node(1)
        root.left.right = Node(2)
        self.assertEqual(first_common_ancestor(t, root.left.left, root.left.right), root.left)
        self.assertEqual(first_common_ancestor(t, root.left.left, root), root)
        self.assertEqual(first_common_ancestor(t, root.left.left, root.right), root)


if __name__ == "__main__":
    unittest.main()
