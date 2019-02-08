import unittest
from linked_list import LinkedList


# Determine whether a linked list is a palindrome.
def is_palindrome(ll):
    half_len = len(ll) // 2
    left_half = []
    curr = ll.head

    for _ in range(half_len):
        left_half.append(curr.item)
        curr = curr.next

    if len(ll) % 2 == 1:
        curr = curr.next

    for _ in range(half_len):
        if left_half.pop() != curr.item:
            return False
        curr = curr.next

    return True


class Test(unittest.TestCase):

    def test(self):
        pal = LinkedList()
        not_pal = LinkedList()
        pal.insert_end(1)
        pal.insert_end(2)
        pal.insert_end(3)
        pal.insert_end(5)
        pal.insert_end(3)
        pal.insert_end(2)
        pal.insert_end(1)
        not_pal.insert_end(1)
        not_pal.insert_end(2)
        not_pal.insert_end(3)
        not_pal.insert_end(5)
        not_pal.insert_end(4)
        not_pal.insert_end(2)
        not_pal.insert_end(1)
        self.assertEqual(is_palindrome(pal), True)
        self.assertEqual(is_palindrome(not_pal),  False)


if __name__ == '__main__':
    unittest.main()