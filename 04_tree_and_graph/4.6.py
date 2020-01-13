import unittest
from tree import Node, BinarySearchTree



# In a binary search tree, find an inorder successor of the given node.
# Let assume that each node has a link pointing their parent.
def find_inorder_successor(n):
    # right_child가 있으면 자신의 오른쪽 subtree의 가장 맨 왼쪽 node
    # 없으면 자신의 부모 중 자기보다 오른쪽에 있는 거 리턴
    if n.right:
        return leftmost_child(n.right)

    child = n
    parent = child.parent
    while parent and child is not parent.left:
        child = parent
        parent = parent.parent
    return parent


def leftmost_child(n):
    if not n.left:
        return n

    return leftmost_child(n.left)

class NodeLingkingParent(Node):
    """ A node class that has a link to the parent node. """
    def __init__(self, item):
        super().__init__(item)
        self._parent = None

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._parent = parent


class BinarySearchTreeWithParent(BinarySearchTree):
    """ A BST class whose nodes have a link of their parents. """
    def __init__(self):
        self._root = None

    def insert(self, item):
        node = NodeLingkingParent(item)
        if self.is_empty():
            self.root = node
        else:
            curr = self.root
            while curr:
                if curr.item >= item:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        node.parent = curr
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        node.parent = curr
                        break


class Test(unittest.TestCase):

    def test_node(self):
        n = NodeLingkingParent(3)
        self.assertEqual(n.item, 3)
        self.assertEqual(n.parent, None)
        n2 = NodeLingkingParent(4)
        n.parent = n2
        self.assertEqual(n.parent, n2)
        self.assertEqual(n.parent.item, 4)
    
    def test_tree(self):
        t = BinarySearchTreeWithParent()
        t.insert(1)
        self.assertEqual(t.root.item, 1)
        t.insert(2)
        self.assertEqual(t.root.right.parent, t.root)

    def test(self):
        t = BinarySearchTreeWithParent()
        t.insert(3)
        root = t.root
        self.assertEqual(find_inorder_successor(root), None)
        t.insert(1)
        self.assertEqual(find_inorder_successor(root), None)
        self.assertEqual(find_inorder_successor(root.left), root)
        t.insert(5)
        self.assertEqual(find_inorder_successor(root), root.right)
        t.insert(0)
        self.assertEqual(find_inorder_successor(root.left.left), root.left)
        t.insert(2)
        self.assertEqual(find_inorder_successor(root.left), root.left.right)
        self.assertEqual(find_inorder_successor(root.left.right), root)
        t.insert(4)
        self.assertEqual(find_inorder_successor(root), root.right.left)
        self.assertEqual(find_inorder_successor(root.right), None)
        self.assertEqual(find_inorder_successor(root.right.left), root.right)
        t.insert(6)
        self.assertEqual(find_inorder_successor(root), root.right.left)
        self.assertEqual(find_inorder_successor(root.right), root.right.right)
        self.assertEqual(find_inorder_successor(root.right.right), None)

        



if __name__ == "__main__":
    unittest.main()
