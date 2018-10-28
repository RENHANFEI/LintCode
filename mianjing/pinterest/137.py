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
        nodes_hash = dict()
        self.getNodes(graph, nodes_hash)
        self.getNeighbors(nodes_hash)
        return nodes_hash[graph]
        
    def getNodes(self, node, nodes_hash):
        if node not in nodes_hash:
            nodes_hash[node] = UndirectedGraphNode(node.label)
            for neighbor in node.neighbors:
                self.getNodes(neighbor, nodes_hash)
            
    def getNeighbors(self, nodes_hash):
        for node, new_node in nodes_hash.items():
            new_node.neighbors = [nodes_hash[neighbor] for neighbor in node.neighbors]
        