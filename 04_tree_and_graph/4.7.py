import unittest
from collections import defaultdict
from graph import GraphUsingList



# When a list of projects and their dependencies are given, find an order of the projects.
# If there is no valid order, return error.
# Dependency - In (a, b), b is dependent on a.
# Example -
# Input:    projects: a, b, c, d, e, f
#           dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
def find_order(projects, dependencies):
    edges = build_graph(projects, dependencies)

    path = topological_sort(projects, edges)
    if path:
        print("path:", path)
        return path
    
    raise RuntimeError("There is no valid order.")
        

def build_graph(vertices, edges):
    # Both two dicts are the same dictionaries. g uses the defaultdict class in the collections module.
    g, dict_practice = defaultdict(dict), {}
    depending_vertices = set()

    # Initialize the dictionaries
    for vertex in vertices:
        g[vertex]
        dict_practice[vertex] = {}

    # Add edges to the dictionaries
    for start, end in edges:
        g[start][end] = 1
        dict_practice[start].update({end: 1})
        depending_vertices.add(end)

    return g


def topological_sort(vertices, edges):
    visited = initialize_visited(vertices)
    topological_order = []

    for v in vertices:
        if not visited[v]:
            _topological_sort(v, edges, visited, topological_order)

    return topological_order


def _topological_sort(vertex, edges, visited, topological_order):
    visited[vertex] = True

    for neighbor in edges[vertex]:
        if not visited[neighbor]:
            _topological_sort(neighbor, edges, visited, topological_order)

    topological_order.insert(0, vertex)


def initialize_visited(vertices):
    visited = {}
    for v in vertices:
        visited[v] = False
    return visited


class Test(unittest.TestCase):

    def test(self):
        projects = {"a", "b", "c", "d", "e", "f"}
        dependencies = {("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")}
        self.assertIsNotNone(find_order(projects, dependencies))

        projects = {"a"}
        dependencies = {}
        self.assertIsNotNone(find_order(projects, dependencies))

        projects = {"a", "b"}
        dependencies = {}
        self.assertIsNotNone(find_order(projects, dependencies))

        projects = {"a", "b", "c"}
        dependencies = {("a", "c")}
        with self.assertRaises(RuntimeError):
            find_order(projects, dependencies)


if __name__ == "__main__":
    unittest.main()
