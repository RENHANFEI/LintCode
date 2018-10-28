from collections import OrderedDict

class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """
    def findRedundantDirectedConnection(self, edges):
        
        parent_child = OrderedDict()    # LIFO
        children = set()
        candidates = []
        for u, v in edges:
            if u in parent_child:
                parent_child[u].append(v)
            else:
                parent_child[u] = [v]
            if v not in parent_child:
                parent_child[v] = []
            if v in children:
                candidates.append((u, v))
            children.add(v)
                
        for candidate in candidates:
            parent, child = candidate
            visited = dict([(p, False) for p in parent_child])
            if self.hasCircle(child, parent, parent_child, visited):
                return parent, child
        
        if candidates:
            return candidates[0]
        
        # find circle
        while edges:
            parent, child = edges.pop()
            # print(parent, child)
            visited = dict([(p, False) for p in parent_child])
            if self.hasCircle(child, parent, parent_child, visited):
                return parent, child
            
    def hasCircle(self, node, parent, parent_child, visited):
        if node == parent:
            return True
        visited[node] = True
        for child in parent_child[node]:
            if self.hasCircle(child, parent, parent_child, visited):
                return True
        