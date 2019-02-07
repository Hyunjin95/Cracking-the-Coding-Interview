import unittest
from linked_list import LinkedList


# Move nodes containing items that are less than x to the left side of the list.
# The node containing x should just be the right side of the list, not exactly between of two sides.
def split_linked_list_by(ll, x):
    curr = ll.head
    ll.tail = ll.head
    
    while curr:
        next_node = curr.next
        curr.next = None
        if curr.item < x:
            curr.next = ll.head
            ll.head = curr
        else:
            ll.tail.next = curr
            ll.tail = curr
        curr = next_node
    
    if ll.tail.next:
        ll.tail.next = None
    

class Test(unittest.TestCase):

    def test(self):
        test_ll = LinkedList()
        test_ll.insert_front(4)
        test_ll.insert_front(1)
        test_ll.insert_front(3)
        test_ll.insert_front(2)
        test_ll.insert_front(5)
        test_ll.insert_front(6)
        test_ll.insert_front(2)
        test_ll.insert_front(1)
        split_linked_list_by(test_ll, 3)
        self.assertEqual(str(test_ll), "1 -> 2 -> 2 -> 1 -> 6 -> 5 -> 3 -> 4")


if __name__ == '__main__':
    unittest.main()