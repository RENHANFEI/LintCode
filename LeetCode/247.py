class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        if n == 1:
            return ["0", "1", "8"]

        strobo_dictionary = {"0":"0", "1":"1", "6":"9", "8":"8"}
        ans = []

        if n % 2 == 0:
            depth = n // 2
            self.dfs(strobo_dictionary, depth, "", ans)
        else:
            depth = (n - 1) // 2
            self.dfs(strobo_dictionary, depth, "0", ans)
            self.dfs(strobo_dictionary, depth, "1", ans)
            self.dfs(strobo_dictionary, depth, "8", ans)

        return ans


    def dfs(self, graph, depth, number, ans):
        if depth == 1:
            for u, v in graph.items():
                if u != v:
                    ans.append(u + number + v)
                    ans.append(v + number + u)
                else:
                    if u != "0":
                        ans.append(u + number + v)
        else:
            for u, v in graph.items():
                if u != v:
                    self.dfs(graph, depth - 1, u + number + v, ans)
                    self.dfs(graph, depth - 1, v + number + u, ans)
                else:
                    self.dfs(graph, depth - 1, u + number + v, ans)

