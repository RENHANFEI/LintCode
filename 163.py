class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
            
        count = [1, 1, 2] + [0] * (n - 2)
        
        for i in range(3, n + 1):   # 2, 3
            for j in range(0, i): # 1, 2; 1, 2, 3
                count[i] += count[j] * count[i-j-1]
                
        return count[n]
            