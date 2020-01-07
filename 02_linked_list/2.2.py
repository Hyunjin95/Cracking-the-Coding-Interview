import unittest
from linked_list import LinkedList


# Find a k-th element from the end in a single linked list.
def kth_element_to_last(ll, k):
    # Assume that the index of the last element is 1.
    if k == 0:
        return None
    
    target = ll.head
    target_after_k = ll.head

    for i in range(k):
        if target_after_k is None:
            return None
        target_after_k = target_after_k.next

    while target_after_k:
        target_after_k = target_after_k.next
        target = target.next
    
    return target.item


class Test(unittest.TestCase):

    def test(self):
        test_ll = LinkedList()
        test_ll.insert_front(5)
        test_ll.insert_front(4)
        test_ll.insert_front(3)
        test_ll.insert_front(2)
        test_ll.insert_front(1)
        self.assertEqual(kth_element_to_last(test_ll, 1), 5)
        self.assertEqual(kth_element_to_last(test_ll, 2), 4)
        self.assertEqual(kth_element_to_last(test_ll, 3), 3)
        self.assertEqual(kth_element_to_last(test_ll, 4), 2)
        self.assertEqual(kth_element_to_last(test_ll, 5), 1)


if __name__ == '__main__':
    unittest.main()