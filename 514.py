import itertools

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):

        if k == 1:
            if n == 1 or n == 2:
                return 1
            else:
                return 0   # impossible
        
        ways = 0
        
        # insert clapboards
        # 0, 1, 2, ..., floor(n/2) 2s
        for i in range(n//2 + 1):
            # for each clapboards-insertion, k * (k-1) * (k-1) ... painting ways
            ways += len(list(itertools.combinations((n-i)*[0], i))) * k * (k-1) ** (n-i-1)
            
        return ways

n = 3
k = 3
sol = Solution()
print(sol.numWays(n,k))
