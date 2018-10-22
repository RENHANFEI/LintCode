class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        
        m = len(A)
        n = len(B)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ans = max(ans, dp[i+1][j+1])
                    
        return ans