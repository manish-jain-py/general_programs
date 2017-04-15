
class Vertex:

    def __init__(self,key):
        self.id = key
        self.neighbors = {}
        self.visited = False

    def add_neighbor(self, vertex, weight=0):
        self.neighbors[vertex.id] = weight
        return vertex

    def remove_neighbor(self, vertex):
        if vertex.id in self.neighbors:
            return self.neighbors.pop(vertex.id)

    def get_all_neighbors(self):
        return self.neighbors.keys()

    def __str__(self):
        return str(self.id) + " Neighbors: " + str([(neighbor, self.neighbors[neighbor]) for neighbor in self.neighbors])

class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        v = Vertex(key)
        self.vertices[key] = v
        self.num_vertices += 1
        return v

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def remove_vertex(self, key):
        return self.vertices.pop(key)

    def get_all_vertices(self):
        return self.vertices.values()

    def get_edge_weight(self, from_vertex, to_vertex):
        return from_vertex.neighbors.get(to_vertex.id)

    def add_edge(self, fromVertex, toVertex, weight=0):
        fromVertex.add_neighbor(toVertex, weight)

    def remove_edge(self, fromVertex, toVertex):
        fromVertex.remove_neighbor(toVertex)

    def __str__(self):
        return str([str(self.vertices[x]) for x in self.vertices])
