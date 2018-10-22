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
        count = 0
        n_island = []
        island_identifiers = [-1] * (n * m)
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for i, op in enumerate(operators):
            op_pos = op.x * m + op.y
            if island_identifiers[op_pos] == -1:
                island_identifiers[op_pos] = op_pos
                count += 1
            
            for d in dirs:
                x, y = op.x + d[0],  op.y + d[1]
                dir_pos = x * m + y
                if x < 0 or x > n - 1 or y < 0 or y > m - 1 or island_identifiers[dir_pos] == -1:
                    continue
                op_id = self.findId(island_identifiers, op_pos)
                dir_id = self.findId(island_identifiers, dir_pos)
                
                if dir_id != op_id:
                    island_identifiers[op_id] = dir_id  # link the roots
                    count -= 1
            
            n_island.append(count)
            
        return n_island
    
    
    def findId(self, ids, pos):
        return pos if ids[pos] == pos else self.findId(ids, ids[pos])
        

''' SECOND
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
        
        n_island = [1]
        islands = {}
        
        for op in operators[1:]:
            in_islands = []
            for island in islands:
                if (op.x, op.y) in island:
                    in_islands.append(island)
                elif op.x < n - 1 and (op.x + 1, op.y) in island:
                    in_islands.append(island)
                elif op.x > 0 and (op.x - 1, op.y) in island:
                    in_islands.append(island)
                elif op.y < m - 1 and (op.x, op.y + 1) in island:
                    in_islands.append(island)
                elif op.y > 0 and (op.x, op.y - 1) in island:
                    in_islands.append(island)
                else:
                    pass
                
            new_land = set()
            for in_island in in_islands:
                islands.remove(in_island)
                new_land = new_land | in_island
            
            new_land = new_land | {(op.x, op.y)}
            islands.append(new_land)
            n_island.append(len(islands))
            
            
        return n_island
'''



''' FIRST
import copy

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

'''