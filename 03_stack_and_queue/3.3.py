import unittest
from abc import ABCMeta
from stack_and_queue import Stack


# Define a stack class made of a set of multiple stacks.
# Each stack has a capacity. Create a new stack if the last stack exceeds its capacity.
class StackWithCapacity(Stack):

    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity
    
    @property
    def capacity(self):
        return self._capacity
    
    def is_full(self):
        if self.size == self.capacity:
            return True
        return False
    
    def pop_front(self):
        try:
            before = self.top
            current = before.next
            
            while current.next:
                before = before.next
                current = before.next
            
            before.next = None
            self.size -= 1
        except AttributeError:
            if self.is_empty():
                print("The stack is empty.")
                return None
            else:
                return self.pop_back()
        else:
            return current.item
        

class SetOfStacks(metaclass=ABCMeta):

    def __init__(self, capacity):
        self._capacity = capacity
        self._stack_list = []

    def __len__(self):
        size = 0
        for stack in self.stack_list:
            size += len(stack)
        return size
    
    def __str__(self):
        return_str = ""
        for i, stack in enumerate(self.stack_list):
            return_str += "stack " + str(i) + ": " + str(stack) + "\n"
        return return_str

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def stack_list(self):
        return self._stack_list
    
    def push(self, item):
        if not self.last_stack() or self.last_stack().is_full():
            new_stack = StackWithCapacity(self.capacity)
            new_stack.push(item)
            self.stack_list.append(new_stack)
        else:
            self.last_stack().push(item)
    
    def pop_back(self):
        try:
            result = self.last_stack().pop_back()
        except AttributeError:
            print("The stack is empty.")
            return None
        else:
            if self.last_stack().is_empty():
                del self.stack_list[-1]
            return result
    
    def last_stack(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list[-1]


# It moves the items of the following stacks. Stacks are always full except the last stack.
class DynamicSetOfStacks(SetOfStacks):

    def pop_back_at(self, index):
        try:
            value = self.stack_list[index].pop_back()
        except IndexError:
            print("The stack " + str(index) + " doesn't exist.")
            return None
        else:
            self.left_shift(index)
            return value
    
    def left_shift(self, start):
        while start < len(self.stack_list) - 1:
            print("start: ", start, "stack_list: ", len(self.stack_list))
            self.stack_list[start].push(self.stack_list[start+1].pop_front())
            start += 1 

        if self.stack_list[-1].is_empty():
            del self.stack_list[-1]


# It doesn't move the items of the other stacks.
class StaticSetOfStacks(SetOfStacks):

    def pop_back_at(self, index):
        try:
            value = self.stack_list[index].pop_back()
        except IndexError:
            print("The stack " + str(index) + " doesn't exist.")
            return None
        else:
            if self.stack_list[index].is_empty():
                del self.stack_list[index]
            return value


class Test(unittest.TestCase):

    def test_static(self):
        static = StaticSetOfStacks(5)
        self.assertEqual(static.pop_back_at(1), None)
        static.push(1)
        static.push(2)
        static.push(3)
        static.push(4)
        static.push(5)
        self.assertEqual(len(static), 5)
        static.push(6)
        static.push(7)
        self.assertEqual(static.pop_back_at(0), 5)
        self.assertEqual(static.pop_back_at(0), 4)
        self.assertEqual(static.pop_back_at(0), 3)
        static.push(8)
        static.push(9)
        static.push(10)
        static.push(11)
        static.push(12)
        static.push(13)
        self.assertEqual(static.pop_back_at(2), 13)
        self.assertEqual(static.pop_back(), 12)
        self.assertEqual(static.pop_back(), 11)
        self.assertEqual(static.pop_back_at(0), 2)
        self.assertEqual(static.pop_back_at(0), 1)
        self.assertEqual(static.pop_back(), 10)
        self.assertEqual(static.pop_back(), 9)
        self.assertEqual(static.pop_back(), 8)
        self.assertEqual(static.pop_back(), 7)
        self.assertEqual(static.pop_back(), 6)
        self.assertEqual(static.pop_back(), None)
        self.assertEqual(static.pop_back_at(0), None)

    def test_dynamic(self):
        dynamic = DynamicSetOfStacks(3)
        dynamic.push(1)
        dynamic.push(2)
        dynamic.push(3)
        dynamic.push(4)
        dynamic.push(5)
        dynamic.push(6)
        self.assertEqual(dynamic.pop_back_at(2), None)
        dynamic.push(7)
        dynamic.push(8)
        dynamic.push(9)
        self.assertEqual(len(dynamic), 9)
        self.assertEqual(dynamic.pop_back_at(2), 9)
        self.assertEqual(dynamic.pop_back_at(2), 8)
        self.assertEqual(dynamic.pop_back_at(2), 7)
        self.assertEqual(dynamic.pop_back_at(0), 3)
        self.assertEqual(dynamic.pop_back_at(0), 4)
        self.assertEqual(dynamic.pop_back_at(0), 5)
        self.assertEqual(dynamic.pop_back_at(0), 6)
        self.assertEqual(dynamic.pop_back_at(0), 2)
        self.assertEqual(dynamic.pop_back_at(0), 1)
        self.assertEqual(dynamic.pop_back_at(0), None)


if __name__ == '__main__':
    unittest.main()


