class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        if n <= 0:
            return
        
        ans = []
        self.gen('', n, 0, 0, ans)
        return ans
        
        
    def gen(self, cur, n, left, right, ans):
      
        if left < n:
            self.gen(cur + '(', n, left + 1, right, ans)
        
        if right < left:
            self.gen(cur + ')', n, left, right + 1, ans)
            
        if left == right == n:
            ans.append(cur)
