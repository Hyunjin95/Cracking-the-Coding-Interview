import unittest
from abc import ABCMeta, abstractmethod
from stack_and_queue import Stack


# Define the class of a queue with two stacks.
class QueueWithDoubleStacks(metaclass=ABCMeta):

    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
    
    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def __str__(self):
        return_str = "in_stack: " + str(self.in_stack) + "\n"
        return_str += "out_stack: " + str(self.out_stack) + "\n"
        return return_str

    @property
    def in_stack(self):
        return self._in_stack
    
    @property
    def out_stack(self):
        return self._out_stack

    @abstractmethod
    def push(self, item):
        pass
    
    @abstractmethod
    def pop_front(self):
        pass

    def push_all_in_from_out(self):
        while len(self.out_stack) > 0:
            self.in_stack.push(self.out_stack.pop_back())
    
    def push_all_out_from_in(self):
        while len(self.in_stack) > 0:
            self.out_stack.push(self.in_stack.pop_back())
    
    def is_empty(self):
        if len(self) == 0:
            return True
        return False


class PushEfficientQueue(QueueWithDoubleStacks):

    def push(self, item):
        self.in_stack.push(item)
    
    def pop_front(self):
        if self.is_empty():
            print("The queue is empty.")
            return None
        if len(self.out_stack) > 0:
            return self.out_stack.pop_back()
        self.push_all_out_from_in()
        return self.out_stack.pop_back()


class PopEfficientQueue(QueueWithDoubleStacks):

    def push(self, item):
        self.push_all_in_from_out()
        self.in_stack.push(item)
        self.push_all_out_from_in()
    
    def pop_front(self):
        if self.is_empty():
            print("The queue is empty.")
            return None
        return self.out_stack.pop_back()


class Test(unittest.TestCase):

    def test_push_efficient(self):
        q = PushEfficientQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)
        self.assertEqual(q.pop_front(), 1)
        self.assertEqual(q.pop_front(), 2)
        q.push(5)
        q.push(6)
        self.assertEqual(q.pop_front(), 3)
        self.assertEqual(q.pop_front(), 4)
        q.push(7)
        self.assertEqual(q.pop_front(), 5)
        self.assertEqual(q.pop_front(), 6)
        self.assertEqual(q.pop_front(), 7)
    
    def test_pop_efficient(self):
        q = PopEfficientQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)
        self.assertEqual(q.pop_front(), 1)
        self.assertEqual(q.pop_front(), 2)
        q.push(5)
        q.push(6)
        self.assertEqual(q.pop_front(), 3)
        self.assertEqual(q.pop_front(), 4)
        q.push(7)
        self.assertEqual(q.pop_front(), 5)
        self.assertEqual(q.pop_front(), 6)
        self.assertEqual(q.pop_front(), 7)


if __name__ == '__main__':
    unittest.main()
