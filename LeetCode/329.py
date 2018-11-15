class Solution:
        
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        memo = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_length = 1
        
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                length = self.dfsPath(matrix, i, j, memo)
                max_length = max(max_length, length)
                
        return max_length
    
    def dfsPath(self, matrix, row, col, memo):
        if memo[row][col] > 0:
            return memo[row][col]
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        length = 1
        
        for i_shift, j_shift in dirs:
            i = row + i_shift
            j = col + j_shift
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= matrix[row][col]:
                continue
            length = max(length, 1 + self.dfsPath(matrix, i, j, memo))
            
        memo[row][col] = length
        
        return length
                
        