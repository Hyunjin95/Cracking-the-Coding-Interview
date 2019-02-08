import unittest


# Define a class that contains three stacks in an array.
class ThreeStacksInArray:

    def __init__(self, stack_size):
        self._stack_size = stack_size
        self._stack_list = [[] for _ in range(self.number_of_stacks())]
        
    def __len__(self):
        return len(self.stack_list[0]) + len(self.stack_list[1]) + len(self.stack_list[2])

    def __str__(self):
        return_str = "stack 0: " + str(self.stack_list[0]) + "\n"
        return_str += "stack 1: " + str(self.stack_list[1]) + "\n"
        return_str += "stack 2: " + str(self.stack_list[2]) + "\n"
        return return_str
    
    @staticmethod
    def number_of_stacks():
        return 3
    
    @property
    def stack_size(self):
        return self._stack_size
    
    @property
    def stack_list(self):
        return self._stack_list
    
    def push(self, stack_num, item):
        if self.is_full(stack_num):
            print("The stack " + str(stack_num) + " is full.")
            return
        self.stack_list[stack_num].append(item)
    
    def pop_at(self, stack_num):
        if self.is_empty(stack_num):
            print("The stack " + str(stack_num) + " is empty.")
            return None
        return self.stack_list[stack_num].pop()
    
    def peek_at(self, stack_num):
        if self.is_empty(stack_num):
            print("The stack " + str(stack_num) + " is empty.")
            return None
        return self.stack_list[stack_num][-1]

    def is_full(self, stack_num):
        if len(self.stack_list[stack_num]) == self.stack_size:
            return True
        return False
    
    def is_empty(self, stack_num):
        if len(self.stack_list[stack_num]) == 0:
            return True
        return False


class Test(unittest.TestCase):

    def test(self):
        s = ThreeStacksInArray(5)
        s.push(0, 1)
        s.push(0, 2)
        s.push(1, 10)
        s.push(1, 11)
        s.push(2, 100)
        s.push(2, 101)
        self.assertEqual(len(s), 6)
        s.push(0, 3)
        s.push(0, 4)
        s.push(0, 5)
        self.assertEqual(s.pop_at(0), 5)
        self.assertEqual(s.pop_at(0), 4)
        self.assertEqual(s.pop_at(0), 3)
        self.assertEqual(s.pop_at(0), 2)
        self.assertEqual(s.pop_at(0), 1)
        self.assertEqual(s.pop_at(0), None)
        self.assertEqual(s.peek_at(0), None)
        self.assertEqual(s.peek_at(1), 11)
        self.assertEqual(s.peek_at(2), 101)
        self.assertEqual(len(s), 4)


if __name__ == '__main__':
    unittest.main()
