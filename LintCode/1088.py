class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """
    def findRedundantConnection(self, edges):
        
        ids = dict()    # store parent to do uf
        for u, v in edges:
            if u in ids:
                if v in ids:
                    if self.findRoot(v, ids) == self.findRoot(u, ids):
                        return u, v
                    else:
                        ids[self.findRoot(v, ids)] = self.findRoot(u, ids)
                else:
                    ids[v] = u
            elif v in ids:
                ids[u] = v
            else:
                ids[u] = u
                ids[v] = u
        
    def findRoot(self, v, ids):
        return v if ids[v] == v else self.findRoot(ids[v], ids)
