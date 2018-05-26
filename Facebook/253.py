"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heappush, heappop, nsmallest

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        
        intervals.sort(key=lambda x:x.start)
        
        pq = []
        
        minrooms = 0
        
        for i in range(len(intervals)):
            if pq != [] and intervals[i].start >= nsmallest(1,pq)[0]:
                heappop(pq)
            heappush(pq,intervals[i].end)

        return len(pq)
