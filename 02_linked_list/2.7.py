import unittest
from linked_list import LinkedList


# Return the first node of the intersection of two linked lists.
def find_intersection(ll1, ll2):
    len1, len2 = len(ll1), len(ll2)
    curr1, curr2 = ll1.head, ll2.head

    if len1 >= len2:
        for i in range(len1 - len2):
            curr1 = curr1.next
        return first_node_of_intersection(curr1, curr2)
    else:
        for i in range(len2 - len1):
            curr2 = curr2.next
        return first_node_of_intersection(curr2, curr1)


def first_node_of_intersection(node1, node2):
    while node1:
        if node1 is node2:
            return node1
        node1 = node1.next
        node2 = node2.next
    return None


class Test(unittest.TestCase):

    def test(self):
        test_ll1 = LinkedList()
        test_ll2 = LinkedList()
        test_ll1.insert_end(1)
        test_ll1.insert_end(2)
        test_ll1.insert_end(3)
        test_ll1.insert_end(4)
        test_ll1.insert_end(5)
        test_ll1.insert_end(6)
        test_ll2.insert_end(11)
        test_ll2.insert_end(12)

        curr1 = test_ll1.head.next.next.next
        curr2 = test_ll2.head.next
        # Now test_ll2 is '11 -> 12 -> 4(test_ll1)'
        curr2.next = curr1
        
        self.assertEqual(find_intersection(test_ll1, test_ll2), curr1)
        curr2.next = None
        self.assertEqual(find_intersection(test_ll1, test_ll2), None)


if __name__ == '__main__':
    unittest.main()

