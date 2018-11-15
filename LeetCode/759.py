# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        
        if not schedule:
            return
        
        intervals = []
        for personal_schedule in schedule:
            intervals.extend(personal_schedule)
            
        intervals.sort(key=lambda interval:(interval.start, interval.end))
        
        ans = []
        pre_end = intervals[0].end
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start > pre_end:
                ans.append([pre_end, start])
            pre_end = max(end, pre_end)
            
        return ans
        