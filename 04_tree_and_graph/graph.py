from abc import ABCMeta, abstractproperty, abstractmethod
from collections import defaultdict
import unittest



class Graph(metaclass=ABCMeta):
    """
        A metaclass for two graph classes: GraphUsingList and GraphUsingMatrix.
    """
    @abstractmethod
    def __init__(self):
        self._graph = None
        self._vertices = set()

    @property
    def graph(self):
        return self._graph
    
    @property
    def vertices(self):
        return self._vertices

    def add_edge(self, n, m, w):
        if n < 0 or m < 0:
            raise RuntimeError("The value of vertices should be greater than 0")
        self.vertices.add(n)
        self.vertices.add(m)
        self.graph[n][m] = w

    def __str__(self):
        return str(self.graph)
    

class GraphUsingList(Graph):
    """
        A directed graph represented with an adjacency list.
    """
    def __init__(self):
        super().__init__()
        self._graph = defaultdict(dict)


class GraphUsingMatrix(Graph):
    """
        A directd graph represented with an adjacency matrix.

        Attributes:
            num_vertices: The number of vertices in the graph.
    """
    def __init__(self, num_vertices):
        super().__init__()
        self._num_vertices = num_vertices
        self._graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    @property
    def num_vertices(self):
        return self._num_vertices

    def add_edge(self, n, m, w):
        limit = self.num_vertices
        if n >= limit or m >= limit:
            raise RuntimeError("The value of vertices should be lower than {}".format(limit))
        super().add_edge(n, m, w)


class Test(unittest.TestCase):
    """ A test class for the graphs """
    def test_graph_list(self):
        g = GraphUsingList()
        g.add_edge(1, 2, 1)
        g.add_edge(1, 3, 2)
        g.add_edge(2, 1, 3)
        g.add_edge(5, 4, 10)
        self.assertEqual(g.graph, defaultdict(dict, {1: {2: 1, 3: 2}, 2: {1: 3}, 5: {4: 10}}))

    def test_graph_matrix(self):
        g = GraphUsingMatrix(5)
        g.add_edge(1, 4, 2)
        g.add_edge(1, 2, 3)
        g.add_edge(3, 1, 2)
        g.add_edge(2, 4, 10)
        g.add_edge(0, 1, 5)
        g.add_edge(4, 0, 10)
        self.assertEqual(g.graph, [[0, 5, 0, 0, 0], [0, 0, 3, 0, 2], [0, 0, 0, 0, 10], [0, 2, 0, 0, 0], [10, 0, 0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
