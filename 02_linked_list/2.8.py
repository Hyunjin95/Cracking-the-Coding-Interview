import unittest
from linked_list import LinkedList


# Return the first node of a circular linked list.
def beginning_of_loop(ll):
    slower, faster = ll.head, ll.head

    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next

        if slower is faster:
            break
    
    slower = ll.head

    while slower and faster:
        if slower is faster:
            return slower
        slower = slower.next
        faster = faster.next

    return None


class Test(unittest.TestCase):

    def test(self):
        test_ll = LinkedList()
        test_ll.insert_end(1)
        test_ll.insert_end(2)
        test_ll.insert_end(3)
        test_ll.insert_end(4)
        test_ll.insert_end(5)
        test_ll.insert_end(6)

        self.assertEqual(beginning_of_loop(test_ll), None)

        curr = test_ll.head
        while curr.next:
            curr = curr.next
        curr.next = test_ll.head.next.next

        self.assertEqual(beginning_of_loop(test_ll).item, 3)


if __name__ == '__main__':
    unittest.main()