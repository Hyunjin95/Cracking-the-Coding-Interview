import unittest
from linked_list import LinkedList


# It's the same as problem 2.5. However, numbers are arranged normally in this problem.
def adder(ll1, ll2):
    len1, len2 = len(ll1), len(ll2)

    if len1 < len2:
        list_padding(ll1, len2 - len1)
    elif len1 > len2:
        list_padding(ll2, len1 - len2)

    sum_list = LinkedList()
    carry = recursive_adder(ll1.head, ll2.head, sum_list)

    if carry > 0:
         sum_list.insert_front(carry)

    return sum_list


def recursive_adder(num1, num2, partial_sum):
    if not num1.next:
        val = num1.item + num2.item
        partial_sum.insert_front(val % 10)
        return val // 10
    
    val = recursive_adder(num1.next, num2.next, partial_sum) + num1.item + num2.item
    partial_sum.insert_front(val % 10)
    return val // 10


def list_padding(ll, number):
    for _ in range(number):
        ll.insert_front(0)


class Test(unittest.TestCase):

    def test(self):
        num1 = LinkedList()
        num2 = LinkedList()
        num1.insert_end(9)
        num1.insert_end(2)
        num1.insert_end(3)
        num1.insert_end(5)
        num2.insert_end(8)
        num2.insert_end(9)
        num2.insert_end(7)
        sum_of_lists = adder(num1, num2)
        self.assertEqual(str(sum_of_lists), "1 -> 0 -> 1 -> 3 -> 2")


if __name__ == '__main__':
    unittest.main()