# Creating graph


class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}

        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)