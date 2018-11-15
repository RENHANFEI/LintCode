class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        num = len(M)
        ids = [i for i in range(num)]
        
        for i in range(num):
            for j in range(i + 1, num):
                if M[i][j] and self.findId(ids, j) != self.findId(ids, i):
                    ids[self.findId(ids, j)] = i

        circles = set()
        for i in range(num):
            circles.add(self.findId(ids, i))
            
        return len(circles)
                    
    def findId(self, ids, i):
        return i if ids[i] == i else self.findId(ids, ids[i])
        
sol = Solution()
M = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
M = [
[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]]
print(sol.findCircleNum(M))