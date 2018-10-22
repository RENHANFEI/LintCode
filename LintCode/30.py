"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        if intervals == []:
            return [newInterval]
        
        if newInterval.start >= intervals[-1].start:
            intervals.append(newInterval)
        else:
            # insert
            for i, interval in enumerate(intervals):
                if newInterval.start <= interval.start:
                    intervals.insert(i, newInterval)
                    break
        
        # merge
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
                
            
        # # traverse intervals to get the position
        # for interval in intervals:
        #     if interval.end < newInterval.start:
        #         newIntervals.append(interval)
        #     elif interval.start > newInterval.end:
        #         newIntervals.append(newInterval)
        #         newIntervals.appned(interval)
        #     else:
        #         # overlapped
        #         if newInterval.start <= interval.start:
        #             if newInterval.end <= interval.end:
        #                 pass
        #             else:
        #                 pass
        #         else:   # new.start > int.start and new.start <= int.end
        #             pass
        