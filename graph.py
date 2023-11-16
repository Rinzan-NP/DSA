class Graph:
    def __init__(self) -> None:
        self.graph = {}


    def add(self, vertex, edge, uni = False):
        if vertex not in self.graph:
            self.graph[vertex] = []
        if edge not in self.graph:
            self.graph[edge] = []
        self.graph[vertex].append(edge)
        if uni is False:
            self.graph[edge].append(vertex)

    def remove_vertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for i in self.graph:
            if i != vertex:
                if vertex in self.graph[i]:
                    self.graph[i].remove(vertex)
            
    
    def find_path(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph:
            return []
        
        paths = []
        for node in self.graph[start]:
            new_paths = self.find_path(node, end, path)
            for new_path in new_paths:
                paths.append(new_path)

        return paths
    
    def depth_first_search(self, start, visited=None):
        if visited is None:
            visited = []

        if start not in self.graph:
            return []
        
        
        if start not in visited:
            visited.append(start)
            for neighbor in self.graph[start]:
                self.depth_first_search(neighbor, visited)

        for vertex in self.graph:
            if vertex not in visited:
                self.depth_first_search(vertex, visited)

        return visited



graph = Graph()

graph.add(1, 3, uni = True)
graph.add(2, 3, uni = True)
graph.add(2, 4, uni = True)
graph.add(3, 4, uni = True)
graph.add(5,6)
start = 1
end = 4
print(graph.graph)
print(graph.depth_first_search(1))

def depth_first_search(self, start, visited=None):
    if visited is None:
        visited = []

    if start not in self.graph:
        return []

    if start not in visited:
        visited.append(start)
        for neighbor in self.graph[start]:
            self.depth_first_search(neighbor, visited)

    for vertex in self.graph:
        if vertex not in visited:
            self.depth_first_search(vertex, visited)

    return visited
