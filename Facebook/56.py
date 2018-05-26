# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if not intervals:
            return []
        
        intervals.sort(key = lambda x:x.start)
        
        res = [intervals[0]]
        
        end = intervals[0].end

    
        for i in range(1,len(intervals)):
            if end >= intervals[i].start:
                end = max(intervals[i].end,end)
            else:
                res.append(intervals[i])
        
                
        return res
        
