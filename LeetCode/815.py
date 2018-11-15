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
        for route_idx, route in enumerate(routes):
            for stop in route:
                pass_bus[stop].add(route_idx)
                
        visited = {S}
        stop_buses = [(S, 0)]
        
        for stop, bus_num in stop_buses:
            if stop == T:
                return bus_num
            for route_idx in pass_bus[stop]:
                for stop in routes[route_idx]:
                    if stop not in visited:
                        stop_buses.append((stop, bus_num + 1))
                pass_bus[route_idx] = []
                        
        return -1
                



sol = Solution()
routes = [[1,2,7],[3,6,7]]
s = 1
t = 6

print(sol.numBusesToDestination(routes, s, t))