# WEEK 1 
# DAY 1


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
          self.adjacency_list[vertex] = []
          return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
          self.adjacency_list[vertex1].append(vertex2)
          self.adjacency_list[vertex2].append(vertex1)
          return True
        
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        
        return False
    

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        from collections import deque

        queue = deque([vertex])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)


    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            last_element = stack.pop()
            if last_element not in visited:
                print(last_element)
                visited.add(last_element)
                for adjacent_vertex in self.adjacency_list[last_element]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)
                
                



    
    

        
    

# custom_graph = Graph()

# custom_graph.add_vertex("A")
# custom_graph.add_vertex("B")
# custom_graph.add_edge("A","B")
# custom_graph.remove_edge("A","B")

# custom_graph.print_graph()

# custom_graph.remove_vertex("A")
# print("----After Remove----")
# custom_graph.print_graph()
custom_graph = Graph()

custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_vertex("D")
custom_graph.add_vertex("E")
print(custom_graph.adjacency_list)

custom_graph.add_edge("A","B")
custom_graph.add_edge("A", "C")
custom_graph.add_edge("B", "E")
custom_graph.add_edge("C","D")
custom_graph.add_edge("D", "E")
print(custom_graph.adjacency_list)

custom_graph.bfs("A")
print("----")
custom_graph.dfs("A")




# def bfs(self, vertex):
#     visited = set()
#     visited.add(vertex)
#     from collections import deque
#     queue = deque([vertex])

#     while queue:
#         current_vertex = queue.pop(0)
#         print(current_vertex)
#         for adjacent_vertex in self.adjacency_list[current_vertex]:
#             if adjacent_vertex not in visited:
#                 visited.add(adjacent_vertex)
#                 queue.append(adjacent_vertex)

