import unittest
from stack_and_queue import Stack


# Sort a stack. Only one additional stack is allowed to use.
def sort_stack(stack):
    sorted_stack = Stack()

    while not stack.is_empty():
        curr_item = stack.pop_back()
        while not sorted_stack.is_empty() and sorted_stack.peek() > curr_item:
            stack.push(sorted_stack.pop_back())
        sorted_stack.push(curr_item)

    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop_back())


class Test(unittest.TestCase):

    def test(self):
        s = Stack()
        s.push(1)
        s.push(3)
        s.push(4)
        s.push(2)
        s.push(5)
        s.push(6)
        s.push(10)
        s.push(8)
        s.push(3)
        s.push(9)
        s.push(7)
        sort_stack(s)
        self.assertEqual(str(s), "1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10")


if __name__ == '__main__':
    unittest.main()