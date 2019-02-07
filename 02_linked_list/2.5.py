import unittest
from linked_list import LinkedList


# Two linked lists are given. Both linked lists represent numbers. Each number is arranged in the reverse order.
# Get the sum of two lists, and return it as a linked list.
def adder_reverse(ll1, ll2):
    len1, len2 = len(ll1), len(ll2)

    if len1 < len2:
        list_padding_reverse(ll1, len2 - len1)
    elif len1 > len2:
        list_padding_reverse(ll2, len1 - len2)

    num1 = ll1.head
    num2 = ll2.head
    sum_list = LinkedList()
    carry = 0

    while num1:
        sum_elements = num1.item + num2.item + carry
        quotient = sum_elements % 10
        carry = sum_elements // 10
        sum_list.insert_end(quotient)

        num1 = num1.next
        num2 = num2.next
    
    return sum_list


def list_padding_reverse(ll, number):
    for _ in range(number):
        ll.insert_end(0)


class Test(unittest.TestCase):

    def test(self):
        num1 = LinkedList()
        num2 = LinkedList()
        num1.insert_front(8)
        num1.insert_front(3)
        num1.insert_front(5)
        num2.insert_front(6)
        num2.insert_front(2)
        num2.insert_front(8)
        num2.insert_front(2)
        sum_of_lists = adder_reverse(num1, num2)
        self.assertEqual(str(sum_of_lists), "7 -> 1 -> 1 -> 7")


if __name__ == '__main__':
    unittest.main()