from collections import defaultdict
class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def numBusesToDestination(self, routes, S, T):
        pass_bus = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                pass_bus[stop].add(i)
                
        visited = {S}
        bfs = [(S, 0)]
        
        while bfs:
            new_bfs = []
            for stop, travels in bfs:
                if stop == T:
                    return travels
                for bus_idx in pass_bus[stop]:
                    route = routes[bus_idx]
                    for available_stop in route:
                        if available_stop not in visited:
                            new_bfs.append((available_stop, travels + 1))
                            visited.add(available_stop)
                    routes[bus_idx] = []
            bfs = new_bfs
                            
        return -1


# class Solution:
#     """
#     @param routes:  a list of bus routes
#     @param S: start
#     @param T: destination
#     @return: the least number of buses we must take to reach destination
#     """
#     def numBusesToDestination(self, routes, S, T):
#         if S == T:
#             return 0
            
#         routes = [set(route) for route in routes]
        
#         min_bus = [-1]
#         visited = [False] * len(routes)
#         memo = dict()
#         self.dfs(routes, S, T, visited, 0, min_bus, memo)
        
#         return min_bus[0]
        
#     def dfs(self, routes, source, target, visited, travels, min_bus, memo):
#         if source in memo:
#             min_bus[0] = min(min_bus[0], travels + memo[source])
#             return
#         for i, route in enumerate(routes):
#             if not visited[i]:
#                 if source in route:
#                     available = route - {source}
#                     if target in available:
#                         memo[source] = travels + 1
#                         if min_bus[0] == -1:
#                             min_bus[0] = travels + 1
#                         else:
#                             min_bus[0] = min(min_bus[0], travels + 1)
#                     else:
#                         for stop in available:
#                             new_visited = visited[:]
#                             new_visited[i] = True
#                             self.dfs(routes, stop, 
#                                     target, new_visited, travels + 1, min_bus, memo)
                
