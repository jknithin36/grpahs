class Graph:
    def __init__(self):
        self.adjaceny_list = {}


    def add_vertex(self,vertex):
        if vertex not in self.adjaceny_list.keys():
            self.adjaceny_list[vertex] = []
            return True
        return False
    

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adjaceny_list.keys() and vertex2 in self.adjaceny_list.keys():
            self.adjaceny_list[vertex1].append(vertex2)
            self.adjaceny_list[vertex2].append(vertex1)
            return True
        return False
    

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjaceny_list.keys() and vertex2 in self.adjaceny_list.keys():
            try:
                self.adjaceny_list[vertex1].remove(vertex2)
                self.adjaceny_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjaceny_list.keys():
            for other_verices in self.adjaceny_list[vertex]:
                self.adjaceny_list[other_verices].remove(vertex)
            del self.adjaceny_list[vertex]
            return True
        
        return False
    









graph = Graph()

print(graph.adjaceny_list)
graph.add_vertex("A")
graph.add_vertex("B")
print(graph.adjaceny_list)
graph.add_edge("A","B")
print(graph.adjaceny_list)
graph.remove_edge("A", "B")
print(graph.adjaceny_list)

graph.add_vertex("D")
print(graph.adjaceny_list)

graph.remove_vertex("D")
print(graph.adjaceny_list)

