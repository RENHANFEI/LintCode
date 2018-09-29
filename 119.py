class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        
        len1, len2 = len(word1), len(word2)
        d = [[0] * (len2 + 1) for _ in range((len1 + 1))]
        
        for i in range(len1 + 1):
            d[i][0] = i
        
        for i in range(len2 + 1):
            d[0][i] = i
        
        for i in range(len1):
            for j in range(len2):
                d[i+1][j+1] = min(\
                        d[i][j] + (0 if word1[i] == word2[j] else 1), \
                        d[i+1][j] + 1, d[i][j+1] + 1)
        
        return d[-1][-1]
