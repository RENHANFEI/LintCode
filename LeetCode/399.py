from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(lambda: dict())
        for i, val in enumerate(values):
            dividend, divider = equations[i]
            graph[dividend][divider] = val
            graph[divider][dividend] = 1 / val
        
        ans = []
        n = len(graph)
        for dividend, divider in queries:
            visited = dict([(node, False) for node in graph])
            print(graph, visited, dividend, divider)
            ans.append(self.dfs(graph, visited, dividend, 1, divider))
        
        return ans
    
    def dfs(self, graph, visited, dividend, val, divider):
        print((visited, dividend, val, divider, dividend in visited))
        if dividend in visited and dividend == divider:
            return val
        visited[dividend] = True
        for node, v in graph[dividend].items():
            if not visited[node]:
                ans = self.dfs(graph, visited, node, val * v, divider)
                if ans != -1:
                    return ans
        return -1

equations = [ ["a","b"],["b","c"] ]
values = [2.0,3.0]
queries = [ ["a","c"],["b","c"],["a","a"] ]

sol = Solution()
print(sol.calcEquation(equations, values, queries))