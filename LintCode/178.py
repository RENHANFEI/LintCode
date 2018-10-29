class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n <= 1 and not edges:
            return True
            
        connect = {i: i for i in range(n)}
        covered = set()
        for u, v in edges:
            if self.find(connect, u) == self.find(connect, v):
                return False
                
            connect[self.find(connect, u)] = v
            covered.add(u)
            covered.add(v)
            
        if len(covered) < n: return False
        return True

    def find(self, ids, node):
        return node if ids[node] == node else self.find(ids, ids[node])
