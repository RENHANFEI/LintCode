import copy

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        if not operators:
            return []
            
        grid = [[0] * m for i in range(n)]
        
        n_island = [1]
        grid[operators[0].x][operators[0].y] = 1
        
        for i, op in enumerate(operators[1:]):
            
            if grid[op.x][op.y] == 1:
                n_island.append(n_island[i])
                continue
            
            else:
                grid_copy = copy.deepcopy(grid)
                
                connected = self.dfs(op.x + 1, op.y, grid_copy) + self.dfs(op.x - 1, op.y, grid_copy) + self.dfs(op.x, op.y + 1, grid_copy) + self.dfs(op.x, op.y - 1, grid_copy)
                
                grid[op.x][op.y] = 1
                num = n_island[i] + 1 - connected
                n_island.append(num)
            
        return n_island
        
    def dfs(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return 0
        
        if grid[x][y] == 1:
            grid[x][y] = 0
            self.dfs(x + 1, y, grid)
            self.dfs(x - 1, y, grid)
            self.dfs(x, y + 1, grid)
            self.dfs(x, y - 1, grid)
            return 1
            
        return 0