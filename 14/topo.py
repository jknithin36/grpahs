from collections import defaultdict
class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberOfVerticles = numberofVertices 


        def add_edge(self, vertex,edge):
            self.graph[vertex].append(edge)

        def topological_sort(self):
            visited = set()
            result =[]

            def dfs(v):
                if v in visited:
                    return
                visited.add(v)
                for neighbour in self.graph[v]:
                    dfs(neighbour)

                result.append(0, v)

            for i in self.graph.keys():
                if i not in visited:
                    dfs(i)

            print(result)

        