from collections import defaultdict

class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        if not edges:
            return [0]
        
        indegrees = defaultdict(lambda: 0)
        connections = defaultdict(lambda: [])
        s = set(range(n))
        
        for v1, v2 in edges:
            indegrees[v1] += 1
            indegrees[v2] += 1
            connections[v1].append(v2)
            connections[v2].append(v1)
        
        q = []
        
        for v, indegree in indegrees.items():
            if indegree == 1:
                q.append(v)
                s.remove(v)
        
        while s:
            new_q = []
            for v in q:
                connection = connections[v]
                for c in connection:
                    if c not in s:
                        continue
                    indegrees[c] -= 1
                    if indegrees[c] == 1:
                        new_q.append(c)
                        s.remove(c)
            q = new_q
            
        return q

'''First Sol'''
# class Solution:
#     """
#     @param n: n nodes labeled from 0 to n - 1
#     @param edges: a undirected graph
#     @return:  a list of all the MHTs root labels
#     """
#     def findMinHeightTrees(self, n, edges):
#         if not edges:
#             return [0]
            
#         connections = defaultdict(lambda: [])
        
#         for v1, v2 in edges:
#             connections[v1].append(v2)
#             connections[v2].append(v1)
        
#         min_height = n
#         ans = []
#         for v, connection in connections.items():
            
#             s = set(connection)
#             s.add(v)
#             height = 1
            
#             flag = True
#             while len(s) < n:
#                 q = []
#                 for vv in connection:
#                     q += connections[vv]
#                     s |= set(connections[vv])
#                 connection = q
#                 height += 1
#                 if height > min_height:
#                     flag = False
#                     break
            
#             if flag:
#                 if height == min_height:
#                     ans.append(v)
                    
#                 if height < min_height:
#                     min_height = height
#                     ans = [v]
                
#         return ans