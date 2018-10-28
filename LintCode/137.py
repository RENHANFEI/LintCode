"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, graph):
        if not graph:
            return
        visited = set()
        nodes_hash = dict()
        self.getNodes(graph, nodes_hash, visited)
        self.getNeighbors(nodes_hash)
        return nodes_hash[graph]
        
    def getNodes(self, node, nodes_hash, visited):
        if node not in visited:
            nodes_hash[node] = UndirectedGraphNode(node.label)
            visited.add(node)
            for neighbor in node.neighbors:
                self.getNodes(neighbor, nodes_hash, visited)
            
    def getNeighbors(self, nodes_hash):
        for node, new_node in nodes_hash.items():
            new_node.neighbors = [nodes_hash[neighbor] for neighbor in node.neighbors]
        