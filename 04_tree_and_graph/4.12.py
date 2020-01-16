import unittest
from tree import BinarySearchTree



# There is a binary tree where the value of each node is an integer (positive or negative).
# We want to count the number of paths that the sum of integers is a specific number.
# Paths do not have to start from the root and end at the leaf nodes, however, it should go downwards.
# That is, you can only move from the parent nodes to the child nodes.
def count_paths(root, target_num):
    if not root:
        return 0
    
    num_paths_from_root = count_paths_from(root, target_num, 0)
    num_paths_from_left = count_paths(root.left, target_num,)
    num_paths_from_right = count_paths(root.right, target_num)

    return num_paths_from_root + num_paths_from_left + num_paths_from_right


def count_paths_from(node, target_num, partial_sum):
    if not node:
        return 0
    
    partial_sum += node.item
    num_paths = 1 if target_num == partial_sum else 0

    num_paths += count_paths_from(node.left, target_num, partial_sum)
    num_paths += count_paths_from(node.right, target_num, partial_sum)

    return num_paths



class Test(unittest.TestCase):
    def test(self):
        t = BinarySearchTree()
        t.insert(0)
        t.insert(0)
        t.insert(0)
        self.assertEqual(count_paths(t.root, 0), 6)
        t.root.item = 1
        self.assertEqual(count_paths(t.root, 1), 3)
        self.assertEqual(count_paths(t.root, 0), 3)


if __name__ == '__main__':
    unittest.main()
