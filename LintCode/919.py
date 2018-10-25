"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        ends = []
        
        for interval in intervals:
            
            if not ends:
                ends.append(interval.end)
            else:
                if ends[0] <= interval.start:
                    heapq.heapreplace(ends, interval.end)
                else:
                    heapq.heappush(ends, interval.end)
                
        return len(ends)