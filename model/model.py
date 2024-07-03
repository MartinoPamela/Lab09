from networkx.algorithms import threshold

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._fermate = DAO.getAllFermate()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f._ID] = f

    def buildGraph(self, threshold):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        edges = DAO.getAllRotteV2()
        for edge in edges:
            w = edge.avgDistance
            a1Object = self._idMap[edge.a1]
            a2Object = self._idMap[edge.a2]
            if w > threshold:
                self._grafo.add_edge(a1Object, a2Object, weight=w)
                print("added edge", edge)

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def getAllEdges(self):
        return self._grafo.edges

    def getAvgDist(self, v1, v2):
        data = self._grafo.get_edge_data(v1, v2)
        return data["weight"]

