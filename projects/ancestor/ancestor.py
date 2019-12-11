from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    path = []
    
    # Building the Graph
    for e in ancestors:
        g.add_edge(e[1], e[0])        

    # Get set of visted nodes from Traversal
    visted = g.dft(starting_node)

    # Doing a search from starting_node to each vertices that is traversed to get longest path
    for v in visted:
        path_to_each = g.dfs(starting_node, v)
        if len(path_to_each) > len(path):
            path = path_to_each

        if len(path_to_each) == len(path) and path_to_each[-1] < path[-1]:
            path = path_to_each

    if len(path) == 1:
        return -1
    
    return path[-1]

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_vertex(8)
g.add_vertex(9)
g.add_vertex(10)
g.add_vertex(11)


# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 10))