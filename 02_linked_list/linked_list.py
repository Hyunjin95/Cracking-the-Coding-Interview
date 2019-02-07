import unittest


class Node:
    
    def __init__(self, item):
        self._item = item
        self._next = None
        self._prev = None

    def __str__(self):
        return str(self.item)
    
    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, new_item):
        self._item = new_item
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_node):
        self._prev = prev_node
    

class LinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
    
    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head_node):
        self._head = head_node
    
    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail_node):
        self._tail = tail_node
    
    def insert_front(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def insert_end(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    

class Test(unittest.TestCase):

    def test(self):
        a = LinkedList()
        a.insert_end(3)
        a.insert_front(2)
        a.insert_front(1)
        a.insert_end(4)
        self.assertEqual(str(a), "1 -> 2 -> 3 -> 4")
        self.assertEqual(len(a), 4)

        i = 1
        for n in a:
            self.assertEqual(str(n), str(i))
            i += 1


if __name__ == '__main__':
    unittest.main()