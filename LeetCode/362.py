from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.hits:
            self.hits.append(timestamp)
        else:
            self.hits.append(timestamp)
            while self.hits and timestamp - self.hits[0] >= 300:
                self.hits.popleft()
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        if not self.hits:
            return 0
        
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)