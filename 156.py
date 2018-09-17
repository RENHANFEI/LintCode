"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
            
        intervals.sort()
            
        pre_interval = intervals[0]
        merged_intervals = []
        
        for interval in intervals[1:]:
            if interval.start <= pre_interval.end:
                if interval.end > pre_interval.end:
                    pre_interval.end = interval.end
            else:
                merged_intervals.append(pre_interval)
                pre_interval = interval
        
        merged_intervals.append(pre_interval)
        
        return merged_intervals