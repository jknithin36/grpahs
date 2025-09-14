# WEEK 1 
# DAY 1

class Graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            self.g_dict = {}

        self.g_dict = g_dict


    def add_edge(self, vertex, edge):
        self.g_dict[vertex].append(edge)


    

custom_dict = {
    "A" : ["B", "C"],
    "B" : ["A", "D", "E"],
    "C": ["A", "E"],
    "D":["E", "F","B"],
    "E":["B","F"],
    "F": ["D","E"]
}

graph = Graph(custom_dict)


print(graph.g_dict)
graph.add_edge("E", "C")
print(graph.g_dict)
