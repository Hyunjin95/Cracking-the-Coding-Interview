import unittest
from graph import GraphUsingList
from queue import Queue



# If a directed graph is given, determine whether there exists a path between two nodes of the graph.
def exists_path(c, a, b):
    if a == b:
        return True
        
    graph, vertices = c.graph, c.vertices
    visited = dict()

    for n in vertices:
        visited[n] = False
    visit(a, b, visited, graph)            
    print("DFS -", visited)

    return visited[b]


def visit(a, b, visited, graph):
    visited[a] = True

    if a == b:
        return True
    
    node_root = graph[a]
    for neighbor in node_root:
        if visited[neighbor] == False:
            found = visit(neighbor, b, visited, graph)
            if found:
                break


# Use BFS
def exists_path_bfs(c, a, b):
    if a == b:
        return True

    graph, vertices = c.graph, c.vertices
    # Act like a queue by using insert() and pop()
    queue = Queue()
    visited = dict()

    for n in vertices:
        visited[n] = False
    visited[a] = True
    queue.put(a)

    while not queue.empty():
        root = queue.get()
        root_node = graph[root]

        if root is b:
            break

        for neighbor in root_node:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
        
    print("BFS -", visited)
    return visited[b]


class Test(unittest.TestCase):

    def test_dfs(self):
        g = GraphUsingList()
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 4, 3)
        g.add_edge(4, 3, 2)

        self.assertEqual(exists_path(g, 1, 3), True)
        self.assertEqual(exists_path(g, 0, 3), True)
        self.assertEqual(exists_path(g, 0, 2), True)
        self.assertEqual(exists_path(g, 0, 4), True)
        self.assertEqual(exists_path(g, 1, 0), False)
        self.assertEqual(exists_path(g, 3, 4), False)

        g.add_edge(6, 1, 3)
        g.add_edge(1, 0, 2)
        g.add_edge(6, 4, 2)

        self.assertEqual(exists_path(g, 6, 0), True)
        self.assertEqual(exists_path(g, 6, 3), True)
        self.assertEqual(exists_path(g, 1, 0), True)
        self.assertEqual(exists_path(g, 4, 6), False)

        g.add_edge(1, 7, 2)
        g.add_edge(7, 8, 2)
        g.add_edge(8, 9, 2)

        self.assertEqual(exists_path(g, 0, 9), True)
        self.assertEqual(exists_path(g, 0, 7), True)
        self.assertEqual(exists_path(g, 0, 1), True)
    
    def test_bfs(self):
        g = GraphUsingList()
        g.add_edge(0, 1, 5)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 4, 3)
        g.add_edge(4, 3, 2)

        self.assertEqual(exists_path_bfs(g, 1, 3), True)
        self.assertEqual(exists_path_bfs(g, 0, 3), True)
        self.assertEqual(exists_path_bfs(g, 0, 2), True)
        self.assertEqual(exists_path_bfs(g, 0, 4), True)
        self.assertEqual(exists_path_bfs(g, 1, 0), False)
        self.assertEqual(exists_path_bfs(g, 3, 4), False)

        g.add_edge(6, 1, 3)
        g.add_edge(1, 0, 2)
        g.add_edge(6, 4, 2)

        self.assertEqual(exists_path_bfs(g, 6, 0), True)
        self.assertEqual(exists_path_bfs(g, 6, 3), True)
        self.assertEqual(exists_path_bfs(g, 1, 0), True)
        self.assertEqual(exists_path_bfs(g, 4, 6), False)

        g.add_edge(1, 7, 2)
        g.add_edge(7, 8, 2)
        g.add_edge(8, 9, 2)

        self.assertEqual(exists_path_bfs(g, 0, 9), True)
        self.assertEqual(exists_path_bfs(g, 0, 7), True)
        self.assertEqual(exists_path_bfs(g, 0, 1), True)



if __name__ == '__main__':
    unittest.main()
    