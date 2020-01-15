import unittest
from tree import BinarySearchTree


# We can build a binary search tree by inserting items in an array one by one from the left.
# If there are no duplicate items in the BST, print all possible arrays able to make that tree.
# Input: a binary search tree / Output: possible arrays
def arrays_making_bst(root):
    result = []

    if not root:
        result.append([])
        return result

    first = []
    first.append(root.item)

    arrays_left = arrays_making_bst(root.left)
    arrays_right = arrays_making_bst(root.right)

    for left in arrays_left:
        for right in arrays_right:
            mixed_list = []
            mix_left_and_right(left, right, first, mixed_list)
            result.extend(mixed_list)

    return result
    

def mix_left_and_right(left, right, temp_result, list_result):
    # The order of items in each list should be kept the same.
    if len(left) == 0 or len(right) == 0:
        result = temp_result[:]
        result.extend(left)
        result.extend(right)
        list_result.append(result)
        return

    head_left = left.pop(0)
    temp_result.append(head_left)
    mix_left_and_right(left, right, temp_result, list_result)
    left.insert(0, head_left)
    temp_result.pop()

    head_right = right.pop(0)
    temp_result.append(head_right)
    mix_left_and_right(left, right, temp_result, list_result)
    right.insert(0, head_right)
    temp_result.pop()


class Test(unittest.TestCase):

    def test(self):
        t = BinarySearchTree()
        t.insert(2)
        t.insert(1)
        t.insert(3)
        self.assertEqual(arrays_making_bst(t.root), [[2, 1, 3], [2, 3, 1]])


if __name__ == "__main__":
    unittest.main()
