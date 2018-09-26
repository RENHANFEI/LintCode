class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        if grid == []:
            return 0
        
        n_row, n_col = len(grid), len(grid[0])
        res = 0
        
        bombs_cols = [0] * n_col
        
        for i in range(n_row):
            for j in range(n_col):
                
                if j == 0 or grid[i][j-1] == 'W':
                    bombs_row = 0
                    for k in range(j, n_col):
                        if grid[i][k] == 'E':
                            bombs_row += 1
                        if grid[i][k] == 'W':
                            break
                    
                if i == 0 or grid[i-1][j] == 'W':
                    bombs_cols[j] = 0
                    for k in range(i, n_row):
                        if grid[k][j] == 'E':
                            bombs_cols[j] += 1
                        if grid[k][j] == 'W':
                            break
                    
                if grid[i][j] == '0' and bombs_row + bombs_cols[j] > res:
                    res = bombs_row + bombs_cols[j]
    
        return res