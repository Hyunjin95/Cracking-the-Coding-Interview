import unittest
from linked_list import LinkedList


# Remove a node in a single linked list. The node is not at the beginning nor the end of the list.
# You can only access the node you are deleting.
def remove_middle_node(node):
    next_node = node.next
    node.item = next_node.item
    node.next = next_node.next


class Test(unittest.TestCase):
    
    def test(self):
        test_ll = LinkedList()
        test_ll.insert_front(5)
        test_ll.insert_front(4)
        test_ll.insert_front(3)
        test_ll.insert_front(2)
        test_ll.insert_front(1)

        curr = test_ll.head
        # Delete 3
        curr = curr.next.next
        remove_middle_node(curr)
        self.assertEqual(str(test_ll), "1 -> 2 -> 4 -> 5")


if __name__ == '__main__':
    unittest.main()
