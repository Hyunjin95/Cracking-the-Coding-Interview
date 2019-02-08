import unittest
from stack_and_queue import Node
from stack_and_queue import Stack


# Implement a stack that the time complexity of push(), pop(), min() of the stack is all O(1).
class NodeMin(Node):

    def __init__(self, item):
        super().__init__(item)
        self._current_min = item
    
    @property
    def current_min(self):
        return self._current_min
    
    @current_min.setter
    def current_min(self, new_min):
        self._current_min = new_min


class StackMin(Stack):

    def __init__(self, item=None):
        super().__init__(item)
        if not item:
            self._top = None
            self._size = 0
        else:
            self._top = NodeMin(item)
            self._size = 1

    def push(self, item):
        new_node = NodeMin(item) 
        new_node.next = self.top

        if not self.is_empty() and new_node.item > self.top.current_min:
            new_node.current_min = self.top.current_min

        self.top = new_node
        self.size += 1
    
    def min(self):
        try:
            min_value = self.top.current_min
        except AttributeError:
            print("The stack is empty.")
            return None
        else:
            return min_value
    

class Test(unittest.TestCase):

    def test(self):
        sm = StackMin()
        self.assertEqual(sm.min(), None)
        sm.push(3)
        self.assertEqual(sm.min(), 3)
        sm.push(7)
        self.assertEqual(sm.min(), 3)
        sm.push(2)
        self.assertEqual(sm.min(), 2)
        sm.push(6)
        self.assertEqual(sm.min(), 2)
        sm.push(4)
        self.assertEqual(sm.min(), 2)
        sm.push(1)
        self.assertEqual(sm.min(), 1)
        self.assertEqual(sm.pop_back(), 1)
        self.assertEqual(sm.pop_back(), 4)
        self.assertEqual(sm.pop_back(), 6)
        self.assertEqual(sm.pop_back(), 2)
        self.assertEqual(sm.pop_back(), 7)
        self.assertEqual(sm.pop_back(), 3)
        self.assertEqual(sm.pop_back(), None)


if __name__ == '__main__':
    unittest.main()
        