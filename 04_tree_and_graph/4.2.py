import unittest



# Minimum Tree: There is an array sorted in ascending order. The items in the array are integers without duplicates.
# Make a binary search tree that has minimum height.
def minimum_tree(arr):
    if len(arr) < 1:
        return

    return build_bst(arr, 0, len(arr)-1)


def build_bst(arr, start, end):
    if end < start:
        return None
    
    mid = arr[(start+end) // 2]
    root = Node(mid)

    root.left = build_bst(arr, start, mid-1)
    root.right = build_bst(arr, mid+1, end)

    return root


def traverse_inorder(node):
    if not node:
        return ""

    if not (node.left or node.right):
        return str(node.item)

    return traverse_inorder(node.left) + " -> " + str(node.item) + " -> " + traverse_inorder(node.right)


def get_height(node):
    if not  node:
        return 0
    
    if not (node.left or node.right):
        return 1
    
    return max(get_height(node.left), get_height(node.right)) + 1


class Node:
    """ A node class for bst """
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



class Test(unittest.TestCase):

    def test(self):
        test_base_0 = []
        test_base_1 = [0]
        test_base_2 = [0, 1]
        test_odd_base = [0, 1, 2]
        test_odd = [0, 1, 2, 3, 4, 5, 6]
        test_even_base = [0, 1, 2, 3]
        test_even = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        test_odd_big = [i for i in range(2**10-1)]
        test_even_big_0 = [i for i in range(2**10-2)]
        test_even_big_1 = [i for i in range(2**10+1002)]

        self.assertEqual(get_height(minimum_tree(test_base_0)), 0)
        self.assertEqual(get_height(minimum_tree(test_base_1)), 1)
        self.assertEqual(get_height(minimum_tree(test_base_2)), 2)
        self.assertEqual(get_height(minimum_tree(test_odd_base)), 2)
        self.assertEqual(get_height(minimum_tree(test_odd)), 3)
        self.assertEqual(get_height(minimum_tree(test_odd_big)), 10)
        self.assertEqual(get_height(minimum_tree(test_even_base)), 3)
        self.assertEqual(get_height(minimum_tree(test_even)), 4)
        self.assertEqual(get_height(minimum_tree(test_even_big_0)), 10)
        self.assertEqual(get_height(minimum_tree(test_even_big_1)), 11)
        
        
        


if __name__ == '__main__':
    unittest.main()