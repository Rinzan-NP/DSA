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


# graph = Graph()
# graph.add(1, 2, uni = True)
# graph.add(1, 3, uni = True)
# graph.add(2, 3, uni = True)
# graph.add(2, 4, uni = True)
# graph.add(3, 4, uni = True)
# start = 1
# end = 4
# print(f"Path from {start} to  {end} are : {graph.find_path(start, end)}")
# print(f"Before deleting : {graph.graph}")
# graph.remove_vertex(4)
# print(f"After deleting 4 : {graph.graph}")