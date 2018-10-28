class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        if not matrix: return True

        # 00 01
        # 10 11
        # 20 21
        
        m, n = len(matrix), len(matrix[0])
        k = min(m, n)

        for i in range(m):
            diag = matrix[i][0]
            for j in range(1, min(m - i, n)):
                if matrix[i + j][j] != diag: return False
        
        for j in range(1, n):
            diag = matrix[0][j]
            for i in range(1, min(n - j, m)):
                if matrix[i][j + i] != diag: return False

        return True

# 11 74  0 93
# 40 11 74  7

matrix = [[11,74,0,93],[40,11,74,7]]
sol = Solution()
print(sol.isToeplitzMatrix(matrix))