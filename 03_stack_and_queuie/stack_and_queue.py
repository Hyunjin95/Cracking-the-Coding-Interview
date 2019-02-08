from abc import ABCMeta
import unittest


class Node:

    def __init__(self, item):
        self._item = item
        self._next = None
    
    def __str__(self):
        return str(self.item)
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, node):
        self._next = node
    
    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, value):
        self._item = value


class Stack:
    """Basic stack class using a linked list."""
    def __init__(self, item=None):
        if not item:
            self._top = None
            self._size = 0
        else:
            self._top = Node(item)
            self._size = 1

    def __iter__(self):
        curr = self.top
        while curr:
            yield curr
            curr = curr.next
    
    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)
    
    def __len__(self):
        return self.size
    
    @property
    def top(self):
        return self._top
    
    @top.setter
    def top(self, new_top):
        self._top = new_top
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, num):
        self._size = num
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop_back(self):
        try:
            top_item = self.top.item
            second = self.top.next
            self.top = second
            self.size -= 1
        except AttributeError:
            print("The stack is empty.")
            return None
        else:
            return top_item
    
    def peek(self):
        try:
            peek_value = self.top.item
        except AttributeError:
            print("The stack is empty.")
            return None
        else:
            return peek_value
    
    def is_empty(self):
        if self.size > 0:
            return False
        return True


class Queue:
    """Basic queue class using a linked list."""
    def __init__(self, item=None):
        if not item:
            self._first = None
            self._last = None
            self._size = 0
        else:
            self._first = Node(item)
            self._last = Node(item)
            self._size = 1
        
    def __iter__(self):
        curr = self.first
        while curr:
            yield curr
            curr = curr.next
    
    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)
    
    def __len__(self):
        return self.size
    
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, new_node):
        self._first = new_node
    
    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, new_node):
        self._last = new_node
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, num):
        self._size = num
    
    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node 
        self.size += 1
    
    def pop_front(self):
        try:
            first_item = self.first.item
            second = self.first.next
            self.first = second
            self.size -= 1
        except AttributeError:
            print("The queue is empty.")
            return None
        else:
            return first_item
    
    def peek(self):
        try:
            peek_value = self.first.item
        except AttributeError:
            print("The queue is empty.")
            return None
        else:
            return peek_value
    
    def is_empty(self):
        if self.size > 0:
            return False
        return True
    

class Test(unittest.TestCase):

    def test_stack(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        self.assertEqual(len(s), 5)
        self.assertEqual(str(s), "5 -> 4 -> 3 -> 2 -> 1")
        self.assertEqual(s.pop_back(), 5)
        self.assertEqual(s.pop_back(), 4)
        self.assertEqual(s.pop_back(), 3)
        self.assertEqual(s.pop_back(), 2)
        self.assertEqual(s.pop_back(), 1)
        self.assertEqual(s.is_empty(), True)
        self.assertEqual(s.pop_back(), None)
    
    def test_queue(self):
        q = Queue()
        self.assertEqual(len(q), 0)
        q.push(1)
        q.push(2)
        q.push(3)
        q.push(4)
        q.push(5)
        self.assertEqual(len(q), 5)
        self.assertEqual(str(q), "1 -> 2 -> 3 -> 4 -> 5")
        self.assertEqual(q.pop_front(), 1)
        self.assertEqual(q.pop_front(), 2)
        self.assertEqual(q.pop_front(), 3)
        self.assertEqual(q.pop_front(), 4)
        self.assertEqual(q.pop_front(), 5)
        self.assertEqual(q.is_empty(), True)
        self.assertEqual(q.pop_front(), None)


if __name__ == '__main__':
    unittest.main()

        

