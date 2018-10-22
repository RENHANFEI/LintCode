class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        
        if not matrix:
            return False
        
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        
        l, r = 0, len(matrix) - 1
        m = (l + r) // 2
        while l + 1 < r:
            if matrix[m][0] > target:
                r = m
            elif matrix[m][-1] < target:
                l = m
            else:
                break
            m = (l + r) // 2
            
        if matrix[m][0] <= target and matrix[m][-1] >= target:
            row = matrix[m]
        else:
            row = matrix[r]
        
        
        l, r = 0, len(row) - 1
        m = (l + r) // 2
        while l + 1 < r:
            if row[m] > target:
                r = m
            elif row[m] < target:
                l = m
            else:
                return True
            m = (l + r) // 2
                
        if row[m] == target or row[r] == target:
            return True
        
        return False