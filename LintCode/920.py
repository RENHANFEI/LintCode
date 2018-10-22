"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True
        
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        
        pre_interval = intervals[0]
        for interval in intervals[1:]:
            if interval.start < pre_interval.end:
                return False
            pre_interval = interval
        
        return True