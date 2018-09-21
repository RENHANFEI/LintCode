class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        num_islands = 0
        
        if grid == []:
            return 0
        
        if isinstance(grid[0],int):
            # just a row
            pre = 0
            for item in grid:
                if item == 1 and pre == 0:
                    num_islands += 1
                pre = item
        
        if isinstance(grid[0],list):
            for i, row in enumerate(grid):
                for j, item in enumerate(row):
                    if item == 0:
                        continue
                    else:
                        if item == 1:
                            # +1 island
                            num_islands += 1
                            # find all adjacent points and mark sea
                            self.traverseIsland(i, j, grid)
        
        return num_islands
        
    def traverseIsland(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            grid[i][j] = 0
            self.traverseIsland(i - 1, j, grid)
            self.traverseIsland(i + 1, j, grid)
            self.traverseIsland(i, j + 1, grid)
            self.traverseIsland(i, j - 1, grid)


sol = Solution()
x = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]
x = [0,1,1,0,1,0]
print(sol.numIslands(x))
