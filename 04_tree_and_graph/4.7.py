import unittest
from collections import defaultdict
from queue import Queue
from graph import GraphUsingList



# When a list of projects and their dependencies are given, find an order of the projects.
# If there is no valid order, return error.
# Dependency - In (a, b), b is dependent on a.
# Example -
# Input:    projects: a, b, c, d, e, f
#           dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
def find_order(projects, dependencies):
    g = build_graph(projects, dependencies)
    edges, list_num_lines = g[0], g[1]

    path = topological_sort(projects, edges, list_num_lines)
    if path and len(path) == len(projects):
        print("path:", path)
        return path
    
    raise RuntimeError("There is no valid order.")
        

def build_graph(vertices, edges):
    # Both two dicts has the same items. g uses the defaultdict class in the collections module.
    g, dict_practice = defaultdict(dict), {}
    list_num_lines = {}

    # Initialize the dictionaries
    for vertex in vertices:
        g[vertex]
        dict_practice[vertex] = {}
        list_num_lines[vertex] = 0

    # Add edges to the dictionaries
    for start, end in edges:
        g[start][end] = 1
        dict_practice[start].update({end: 1})
        list_num_lines[end] += 1

    return (g, list_num_lines)


def topological_sort(vertices, edges, list_num_lines):
    q = Queue()
    list_order = []

    for v in list_num_lines:
        if list_num_lines[v] == 0:
            q.put(v)
    
    while not q.empty():
        curr = q.get()
        list_order.append(curr)

        for neighbor in edges[curr]:
            list_num_lines[neighbor] -= 1
            if list_num_lines[neighbor] == 0:
                q.put(neighbor)

    return list_order


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
        self.assertIsNotNone(find_order(projects, dependencies))

        projects = {"a", "b", "c"}
        dependencies = {("a", "c"), ("a", "b"), ("c", "a")}
        with self.assertRaises(RuntimeError):
            find_order(projects, dependencies)

        projects = {"a", "b", "c"}
        dependencies = {("b", "c"), ("c", "b")}
        with self.assertRaises(RuntimeError):
            find_order(projects, dependencies)
        
        projects = {"a", "b", "c"}
        dependencies = {("a", "b"), ("b", "c"), ("c", "b")}
        with self.assertRaises(RuntimeError):
            find_order(projects, dependencies)


if __name__ == "__main__":
    unittest.main()
