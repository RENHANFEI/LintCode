#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        
        start = 1
        end = n
        
        if SVNRepo.isBadVersion(1):
            return 1
        
        for _ in range(n):
            
            if SVNRepo.isBadVersion((start + end) // 2):
                end = (start + end) // 2
            else:
                start = (start + end) // 2
                
            if start == end - 1:
                return end
                    
        return n