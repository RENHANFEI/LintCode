class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        x = matrix[0][0]
        for i in range(1, min(len(matrix), len(matrix[0]))):
            if matrix[i][i] != x:
                return False
        return True