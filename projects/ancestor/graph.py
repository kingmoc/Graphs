from util import Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()
            
            if v not in visited:
                # print(v)
                visited.add(v)

                for neighbor in self.vertices[v]:
                    s.push(neighbor)

        return visited
    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = []
        path.append(starting_vertex)
        s.push(path)
        visited = set()
        
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            
            if v not in visited:
                if v == destination_vertex: 
                    return path
                visited.add(v)
                for neighbor in self.vertices[v]:
                    copy_path = path.copy()
                    copy_path.append(neighbor)
                    s.push(copy_path)