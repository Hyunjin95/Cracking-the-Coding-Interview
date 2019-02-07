import unittest
from linked_list import LinkedList


# Remove duplicate items in a unsorted linked list. Temporary buffers cannot be used.
def remove_duplicate(ll):
    slower = ll.head
    while slower:
        faster = slower
        while faster.next:
            if faster.next.item == slower.item:
                faster.next = faster.next.next
            else:
                faster = faster.next
        slower = slower.next


class Test(unittest.TestCase):

    def test(self):
        test_ll = LinkedList()
        test_ll.insert_front(1)
        test_ll.insert_front(3)
        test_ll.insert_front(2)
        test_ll.insert_front(1)
        test_ll.insert_front(5)
        remove_duplicate(test_ll)
        self.assertEqual(str(test_ll), "5 -> 1 -> 2 -> 3")


if __name__ == '__main__':
    unittest.main()